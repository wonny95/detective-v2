"""Build the artifact copy of the game.

usage: python -I build.py <project dir> <out dir> <title> [--hide-dev]

- copies index.html with the given <title>, without the <!doctype>/<html>/<head>/<body> wrapper tags
  (the artifact host adds its own document skeleton)
- keeps the test buttons outside the phone frame (user decision); --hide-dev hides them
- finds every assets/... and audio/... file the page references and writes files.json:
  {"<published path>": "<absolute source path>"} for the Artifact tool's `files`
- prints the page path, the file count and the total size, and fails on a missing file or a size limit
"""
import json, os, re, sys

project, out, title = sys.argv[1], sys.argv[2], sys.argv[3]
keep_dev = '--hide-dev' not in sys.argv[4:]

src = open(os.path.join(project, 'index.html'), encoding='utf-8').read()

html, n = re.subn(r'<title>.*?</title>', f'<title>{title}</title>', src, count=1)
assert n == 1, 'no <title> in index.html'
for tag in (r'<!doctype html>\s*', r'<html[^>]*>\s*', r'</html>\s*', r'<head>\s*', r'</head>\s*', r'<body[^>]*>\s*', r'</body>\s*'):
    html = re.sub(tag, '', html, count=1, flags=re.I)
if not keep_dev:
    # the handlers stay (their buttons still exist); the buttons are just not shown
    html = html.replace('</style>', '.devtools{display:none!important}\n</style>', 1)

# comments can name files loosely (e.g. "tack-red/-grey.webp"), so only the code is scanned
code = re.sub(r'/\*.*?\*/|<!--.*?-->|^[ \t]*//[^\n]*', '', html, flags=re.S | re.M)
EXT = r'\.(?:png|jpe?g|webp|svg|mp3|wav|ogg|woff2)'
refs = set()
# a folder kept in a constant (`const XM = 'assets/places/christmas/'`, then `${XM}tree.jpg`, `XM + g.src`): its uses are
# read with the folder written in, and every file in that folder goes along (some names come from data)
for name, folder in re.findall(r"const ([A-Z_][A-Z0-9_]*) = '((?:assets|audio)/[\w./-]*/)'", code):
    code = code.replace('${%s}' % name, folder)
    base = os.path.join(project, *folder.strip('/').split('/'))
    refs.update(folder + f for f in os.listdir(base) if re.search(EXT + '$', f) and 'original' not in f)
refs.update(re.findall(r'(?:assets|audio)/[\w./-]+?' + EXT, code))
# paths built in a template: a choice between quoted words (`tack-${locked ? 'grey' : 'red'}.webp`) gives those
# files; a plain variable (`audio/words/${file}.wav`) gives every file in that folder that fits the fixed start and end
for head, expr, tail in re.findall(r'((?:assets|audio)/[\w./-]*)\$\{([^}`]*)\}([\w./-]*?' + EXT + ')', code):
    # only the words a choice gives (after ? or :), not the ones it tests (`has('lit') ? '-lit' : ''`,
    # `id === 'badger' ? 'sgt-badger' : id`)
    # a choice can also give a variable (`FACE_ICONS.includes(id) ? id : 'pending'`): then the folder is searched too
    words = re.findall(r"[?:]\s*'([\w./-]*)'", expr) if '?' in expr else re.findall(r"'([\w./-]*)'", expr)
    variable = '?' in expr and re.search(r"[?:]\s*[A-Za-z_$][\w$.]*\s*(?=:|$)", expr)
    if words:
        refs.update(head + w + tail for w in words)
        if not variable: continue
    folder, start = head.rsplit('/', 1)
    names = os.listdir(os.path.join(project, *folder.split('/')))
    # Higgsfield originals sit beside the pictures in the same folders but the page never shows them
    refs.update(f'{folder}/{f}' for f in names if f.startswith(start) and f.endswith(tail) and '/' not in tail and 'original' not in f)
refs = sorted(refs)
files, missing, total = {}, [], len(html.encode('utf-8'))
for ref in refs:
    path = os.path.join(project, *ref.split('/'))
    if not os.path.isfile(path):
        missing.append(ref)
        continue
    size = os.path.getsize(path)
    if size > 15 * 1024 * 1024:
        sys.exit(f'too large for one artifact file (15MB): {ref} {size}')
    files[ref] = os.path.abspath(path).replace('\\', '/')
    total += size
if missing:
    sys.exit('referenced but missing: ' + ', '.join(missing))

# An artifact version holds at most 511 files and one publish at most 255 files / 64MB. The game has hundreds of short
# recordings, so those set from script (not an <audio src> in the markup) go into a few packs of data: URIs, and a
# small script at the top of the page swaps a pack's data in when the game sets an <audio>'s src to one of them
# (the getter still returns the path the game set, and play() waits for a pack still loading).
os.makedirs(out, exist_ok=True)
markup = set(re.findall(r'<audio[^>]*\ssrc="([^"]+)"', html))
packable = [r for r in files if r.startswith('audio/') and r not in markup]
MIME = {'.mp3': 'audio/mpeg', '.wav': 'audio/wav', '.ogg': 'audio/ogg'}
packs, index, cur, cur_size = [], {}, {}, 0
def flush():
    global cur, cur_size
    if cur: packs.append(cur)
    cur, cur_size = {}, 0
import base64
for ref in sorted(packable):
    raw = open(files[ref], 'rb').read()
    if cur_size + len(raw) > 6 * 1024 * 1024: flush()
    cur[ref] = f'data:{MIME[os.path.splitext(ref)[1]]};base64,' + base64.b64encode(raw).decode()
    cur_size += len(raw)
    index[ref] = len(packs)
flush()
os.makedirs(os.path.join(out, 'audio-pack'), exist_ok=True)
for n, pack in enumerate(packs):
    path = os.path.join(out, 'audio-pack', f'{n}.json')
    json.dump(pack, open(path, 'w', encoding='utf-8'), separators=(',', ':'))
for ref in packable: del files[ref]
for n in range(len(packs)): files[f'audio-pack/{n}.json'] = os.path.abspath(os.path.join(out, 'audio-pack', f'{n}.json')).replace(chr(92), '/')
shim = """<script>(() => {
const INDEX = %s, loaded = {}, loading = {}, set = new WeakMap(), wait = new WeakMap();
const load = n => loading[n] ||= fetch(`audio-pack/${n}.json`).then(r => r.json()).then(j => loaded[n] = j);
const M = HTMLMediaElement.prototype, src = Object.getOwnPropertyDescriptor(M, 'src'), play = M.play;
Object.defineProperty(M, 'src', { configurable:true, enumerable:true,
  get(){ return set.has(this) ? set.get(this) : src.get.call(this); },
  set(v){
    const n = INDEX[v];
    if(n === undefined){ set.delete(this); wait.delete(this); return src.set.call(this, v); }
    set.set(this, v);
    if(loaded[n]){ wait.delete(this); return src.set.call(this, loaded[n][v]); }
    wait.set(this, load(n).then(j => { if(set.get(this) === v) src.set.call(this, j[v]); }));
  } });
M.play = function(){ const w = wait.get(this); if(w){ wait.delete(this); return w.then(() => play.call(this)); } return play.call(this); };
})();</script>
""" % json.dumps(index, separators=(',', ':'))
html = html.replace('<script>', shim + '<script>', 1)

total = len(html.encode('utf-8')) + sum(os.path.getsize(v) for v in files.values())
if len(files) > 511 or total > 256 * 1024 * 1024:
    sys.exit(f'too much for one artifact: {len(files)} files, {total} bytes')
# split into publishes of at most 255 files / 60MB each (later publishes to the same url add to the files already there)
chunks, chunk, size = [], {}, 0
for ref, path in files.items():
    n = os.path.getsize(path)
    if chunk and (len(chunk) >= 250 or size + n > 60 * 1024 * 1024):
        chunks.append(chunk); chunk, size = {}, 0
    chunk[ref] = path; size += n
if chunk: chunks.append(chunk)

page = os.path.join(out, 'index.html')
open(page, 'w', encoding='utf-8').write(html)
json.dump(files, open(os.path.join(out, 'files.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for n, c in enumerate(chunks, 1):
    json.dump(c, open(os.path.join(out, f'files-{n}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({'page': page.replace(chr(92), '/'), 'files': len(files), 'audio_packed': len(packable), 'packs': len(packs),
                  'publishes': len(chunks), 'total_mb': round(total / 1048576, 1),
                  'dev_buttons': 'shown' if keep_dev else 'hidden'}, ensure_ascii=False))

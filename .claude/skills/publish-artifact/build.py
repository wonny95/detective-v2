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
# paths built in a template, with any number of ${...} (`audio/violin/${id}-${k}.mp3`): the template becomes a pattern
# and every file under its folder that fits goes along. A choice between quoted words (`tack-${locked ? 'grey' :
# 'red'}.webp`) fits only those words, never the ones it tests (`has('lit') ? '-lit' : ''`, `id === 'badger' ?
# 'sgt-badger' : id`); a choice that can also give a variable (`FACE_ICONS.includes(id) ? id : 'pending'`) or a plain
# variable fits any name. Higgsfield originals sit beside the pictures in the same folders but the page never shows them.
def choice(expr):
    words = re.findall(r"[?:]\s*'([\w./-]*)'", expr) if '?' in expr else re.findall(r"^\s*'([\w./-]*)'\s*$", expr)
    variable = not words or ('?' in expr and re.search(r"[?:]\s*[A-Za-z_$][\w$.]*\s*(?=:|$)", expr))
    return '(?:' + '|'.join([re.escape(w) for w in words] + ([r'[\w.-]*'] if variable else [])) + ')'
for lit in re.findall(r'`([^`]*)`', code):
    for t in re.findall(r'((?:assets|audio)/(?:[\w./-]|\$\{[^}]*\})*?' + EXT + ')', lit):
        if '${' not in t: continue
        parts = re.split(r'\$\{([^}]*)\}', t)
        pattern = re.compile(''.join(re.escape(p) if i % 2 == 0 else choice(p) for i, p in enumerate(parts)))
        folder = parts[0].rsplit('/', 1)[0]
        for root, _, names in os.walk(os.path.join(project, *folder.split('/'))):
            rel = os.path.relpath(root, project).replace(os.sep, '/')
            refs.update(f'{rel}/{f}' for f in names if 'original' not in f and pattern.fullmatch(f'{rel}/{f}'))
# recordings are packed (below), so every one in audio/ goes along: some paths come from folders chosen at run time
# (`${DEDUCE_DIR}${key}.mp3`), and a recording left out would be a silent line
for root, _, names in os.walk(os.path.join(project, 'audio')):
    rel = os.path.relpath(root, project).replace(os.sep, '/')
    refs.update(f'{rel}/{f}' for f in names if re.search(EXT + '$', f) and 'original' not in f)
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
# recordings, so those set from script (not an <audio src> in the markup) go into a few packs: the recordings' bytes
# one after another (published as .mp3 so the host serves them; the page reads the bytes, not the type). A small script
# at the top of the page cuts a pack into blob: URLs and swaps one in when the game sets an <audio>'s src to its path
# (the getter still returns the path the game set, play() waits for a pack still loading, and fetch() of a packed path
# answers from the pack). All packs load in the background once the page is up.
os.makedirs(out, exist_ok=True)
markup = set(re.findall(r'<audio[^>]*\ssrc="([^"]+)"', html))
packable = [r for r in files if r.startswith('audio/') and r not in markup]
MIME = {'.mp3': 'audio/mpeg', '.wav': 'audio/wav', '.ogg': 'audio/ogg'}
packs, index, cur = [], {}, bytearray()
for ref in sorted(packable):
    raw = open(files[ref], 'rb').read()
    if cur and len(cur) + len(raw) > 6 * 1024 * 1024:
        packs.append(cur); cur = bytearray()
    index[ref] = [len(packs), len(cur), len(raw), MIME[os.path.splitext(ref)[1]]]
    cur += raw
if cur: packs.append(cur)
os.makedirs(os.path.join(out, 'audio-pack'), exist_ok=True)
for n, pack in enumerate(packs):
    open(os.path.join(out, 'audio-pack', f'{n}.mp3'), 'wb').write(pack)
for ref in packable: del files[ref]
for n in range(len(packs)): files[f'audio-pack/{n}.mp3'] = os.path.abspath(os.path.join(out, 'audio-pack', f'{n}.mp3')).replace(chr(92), '/')
shim = """<script>(() => {
const INDEX = %s, urls = {}, loading = {}, set = new WeakMap(), wait = new WeakMap();
// #audiodebug on the artifact link shows what each sound did, at the bottom of the page. The host hands the hash over
// after the page has started and the test buttons reload the page, so it is checked at each line and kept for the tab.
const t0 = performance.now(), lines = [];
let on = false;
try { on = sessionStorage.getItem('audiodebug') === '1'; } catch {}
const show = () => { if(!on && location.hash === '#audiodebug'){ on = true; try { sessionStorage.setItem('audiodebug', '1'); } catch {} }
  if(!on || !document.body) return;
  const box = document.getElementById('audioDebug') || document.body.appendChild(Object.assign(document.createElement('pre'), { id:'audioDebug',
    style:'position:fixed;left:0;right:0;bottom:0;z-index:99999;margin:0;max-height:40vh;overflow:auto;font:11px/1.3 monospace;background:#000c;color:#9f9;padding:6px;white-space:pre-wrap;pointer-events:none' }));
  box.textContent = lines.join('\\n'); };
addEventListener('hashchange', show);
const log = (...a) => { lines.push(`${((performance.now() - t0) / 1000).toFixed(1)}s ${a.join(' ')}`); if(lines.length > 25) lines.shift(); show(); };
// a pack's recordings become blob: URLs (the game seeks in them and plays one sentence with #t=start,end)
const realFetch = window.fetch.bind(window);
const load = n => loading[n] ||= (log('pack', n, 'loading'), realFetch(`audio-pack/${n}.mp3`)
  .then(r => { if(!r.ok) throw new Error('http ' + r.status); return r.arrayBuffer(); })
  .then(b => { for(const k in INDEX){ const [p, at, len, type] = INDEX[k];
      if(p === n) urls[k] = URL.createObjectURL(new Blob([b.slice(at, at + len)], { type })); }
    log('pack', n, 'ready'); },
    e => { log('pack', n, 'FAILED', e); delete loading[n]; throw e; }));
const base = location.href.replace(/[#?].*$/, '').replace(/[^/]*$/, '');
const parse = v => { let s = String(v); if(s.startsWith(base)) s = s.slice(base.length);
  const i = s.indexOf('#'); return i < 0 ? [s, ''] : [s.slice(0, i), s.slice(i)]; };
const M = HTMLMediaElement.prototype, src = Object.getOwnPropertyDescriptor(M, 'src'), play = M.play;
Object.defineProperty(M, 'src', { configurable:true, enumerable:true,
  get(){ return set.has(this) ? set.get(this) : src.get.call(this); },
  set(v){
    const [path, frag] = parse(v), n = INDEX[path]?.[0];
    if(n === undefined){ set.delete(this); wait.delete(this); return src.set.call(this, v); }
    set.set(this, v);
    if(urls[path]){ wait.delete(this); return src.set.call(this, urls[path] + frag); }
    wait.set(this, load(n).then(() => { if(set.get(this) === v) src.set.call(this, urls[path] + frag); }));
  } });
M.play = function(){
  const name = String(this.src).split('/').pop(), w = wait.get(this);
  log('play', name, navigator.userActivation?.isActive ? 'in tap' : 'later', w ? 'waits for pack' : '');
  const p = w ? (wait.delete(this), w.then(() => play.call(this))) : play.call(this);
  Promise.resolve(p).then(() => log('playing', name), e => log('play FAILED', name, e?.name, e?.message));
  return p;
};
// the game also fetches a recording to play one sentence of it
window.fetch = function(input, init){
  const [path] = parse(typeof input === 'string' ? input : input?.url ?? ''), n = INDEX[path]?.[0];
  if(n === undefined) return realFetch(input, init);
  return load(n).then(() => realFetch(urls[path]));
};
for(const ev of ['error', 'ended']) document.addEventListener(ev, e => e.target instanceof HTMLMediaElement &&
  log(ev, String(e.target.src).split('/').pop(), e.target.error?.code ?? ''), true);
// load every pack once the page is up, one at a time, so a sound starts right on the tap that asks for it (a browser
// may refuse a sound that starts seconds after the tap, while its pack was still downloading)
addEventListener('load', () => setTimeout(() => [...new Set(Object.values(INDEX).map(e => e[0]))]
  .reduce((p, n) => p.then(() => load(n).catch(() => {})), Promise.resolve()), 1500));
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

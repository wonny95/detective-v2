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

refs = sorted(set(re.findall(r'(?:assets|audio)/[\w./-]+?\.(?:png|jpe?g|webp|svg|mp3|wav|ogg)', html)))
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
if len(files) > 255 or total > 64 * 1024 * 1024:
    sys.exit(f'too much for one publish: {len(files)} files, {total} bytes (split it over several publishes)')

os.makedirs(out, exist_ok=True)
page = os.path.join(out, 'index.html')
open(page, 'w', encoding='utf-8').write(html)
json.dump(files, open(os.path.join(out, 'files.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({'page': page.replace('\\', '/'), 'files': len(files), 'total_mb': round(total / 1048576, 1),
                  'dev_buttons': 'shown' if keep_dev else 'hidden'}, ensure_ascii=False))

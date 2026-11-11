"""Cut Holly's and May's talk poses (stopped working, looking at the detective) out of their Higgsfield sheet.

usage: python scripts/cut-christmas-talk.py
  reads assets/characters/holly-mae-talk-higgsfield-original.png (flat magenta background), writes
  assets/characters/<holly|mae>-talk.png the same way as cut-christmas-backs.py (magenta keyed out, each figure by its
  columns of opaque pixels, trimmed with a 3% margin, 700 px high).
"""
import importlib.util, sys
sys.argv[1:] = ["."]   # cut-christmas-assets reads its download folder at import
from PIL import Image

spec = importlib.util.spec_from_file_location('cut', 'scripts/cut-christmas-assets.py')
cut = importlib.util.module_from_spec(spec); spec.loader.exec_module(cut)

src = Image.open('assets/characters/holly-mae-talk-higgsfield-original.png').convert('RGBA')
px = src.load()
w, h = src.size
for y in range(h):
    for x in range(w):
        r, g, b, _ = px[x, y]
        m = min(r, b) - g
        if m > 120: px[x, y] = (0, 0, 0, 0)
        elif m > 50:
            a = round(255 * (120 - m) / 70)
            k = min(r, b) - max(g, 0)
            px[x, y] = (max(0, r - k // 2), g, max(0, b - k // 2), a)
for name, (x0, x1) in zip(['holly', 'mae'], cut.opaque_runs(src, 0, 12)):
    fig = cut.trim(src.crop((x0, 0, x1, h)), height=700)
    fig.save(f'assets/characters/{name}-talk.png')
    print(name, x0, x1, fig.size)

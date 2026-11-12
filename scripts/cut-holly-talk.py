"""Cut Holly's talk pose (redrawn as plump as her working pose, user request) out of its Higgsfield picture.

usage: python scripts/cut-holly-talk.py
  reads assets/characters/holly-talk2-higgsfield-original.png (one figure on flat magenta), writes
  assets/characters/holly-talk.png the same way as cut-christmas-talk.py (magenta keyed out, trimmed with a 3% margin,
  700 px high). Replaces the slimmer talk pose cut from holly-mae-talk-higgsfield-original.png.
"""
import importlib.util, sys
sys.argv[1:] = ["."]   # cut-christmas-assets reads its download folder at import
from PIL import Image

spec = importlib.util.spec_from_file_location('cut', 'scripts/cut-christmas-assets.py')
cut = importlib.util.module_from_spec(spec); spec.loader.exec_module(cut)

src = Image.open('assets/characters/holly-talk2-higgsfield-original.png').convert('RGBA')
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
fig = cut.trim(src, height=700)
fig.save('assets/characters/holly-talk.png')
print('holly', fig.size)

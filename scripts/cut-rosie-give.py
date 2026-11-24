"""Rosie holding the blue bag out (picnic case, user request 2026-11-24: shown before she hands it over): the Higgsfield
picture on flat magenta (assets/characters/rosie-give-higgsfield-original.png, job ba656f25) ->
assets/characters/rosie-give.png, the magenta keyed out (with despill like cut-ella-give.py), cut at the same size
(316x661) and place as rosie-higgsfield.png: the figure is drawn at the same scale (658 px tall vs 661) and the head
row at the glasses is 255 px wide in both, so only a crop, centred on her head (x 690.5 -> 161.5).

Run: python -I scripts/cut-rosie-give.py   (Pillow only)
"""
import os
from PIL import Image
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'characters') + '/'
src = Image.open(D + 'rosie-give-higgsfield-original.png').convert('RGB')
W, H = src.size
px = src.load()
out = Image.new('RGBA', src.size)
op = out.load()
for y in range(H):
    for x in range(W):
        r, g, b = px[x, y]
        mag = min(r, b) - g
        a = 255 if mag < 60 else max(0, 255 - int((mag - 60) * 255 / 70))
        if a < 255 and mag > 0:
            k = min(r, b) - (g + 25)
            if k > 0: r, b = r - k, b - k
        op[x, y] = (r, g, b, a)
# the outline next to the background is the dark line blended with magenta (purple, fully opaque): within a few px
# of the background, pull red and blue down to the green+25 the line has inside (her lavender overalls lie further in)
from PIL import ImageFilter
near = out.getchannel('A').point(lambda v: 255 if v < 200 else 0).filter(ImageFilter.MaxFilter(7))
nb = near.load()
for y in range(H):
    for x in range(W):
        if nb[x, y]:
            r, g, b, a = op[x, y]
            k = min(r, b) - (g + 10)
            if k > 0: op[x, y] = (r - k, g, b - k, a)
X0, Y0 = 529, 55
fig = out.crop((X0, Y0, X0 + 316, Y0 + 661))
fig.save(D + 'rosie-give.png', optimize=True)
fig.save(D + 'rosie-give.webp', quality=90, method=6)
print('rosie-give', fig.size, 'figure', fig.getchannel('A').point(lambda v: 255 if v > 40 else 0).getbbox())

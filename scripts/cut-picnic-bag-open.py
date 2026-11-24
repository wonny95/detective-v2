"""The blue bag open (picnic case, user request 2026-11-24: look into the bag Rosie gives before it goes into 소지품): the
Higgsfield picture on flat magenta (assets/places/picnic-storyboard/bag-blue-open-higgsfield-original.png, job 63bd3ada)
-> bag-blue-open.png/.webp, the magenta keyed out with despill (as cut-rosie-give.py), cut to the bag and made 420 px
tall like bag-blue.png (the closed bag), so the two stand at the same size in the close look.
Ben's own blue bag open (user request 2026-11-24: Mia left out, Ben's bag looked into instead): the same picture with a
brown book and a hammer inside (bag-ben-open-higgsfield-original.png, job 007c5d94, the first as reference) ->
bag-ben-open.png/.webp, cut the same way.

Run: python -I scripts/cut-picnic-bag-open.py   (Pillow only)
"""
import os
from PIL import Image, ImageFilter
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'places', 'picnic-storyboard') + '/'
for name in ('bag-blue-open', 'bag-ben-open'):
    src = Image.open(D + name + '-higgsfield-original.png').convert('RGB')
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
    # the outline next to the background blended with magenta: within a few px of it, pull red and blue down
    near = out.getchannel('A').point(lambda v: 255 if v < 200 else 0).filter(ImageFilter.MaxFilter(7))
    nb = near.load()
    for y in range(H):
        for x in range(W):
            if nb[x, y]:
                r, g, b, a = op[x, y]
                k = min(r, b) - (g + 10)
                if k > 0: op[x, y] = (r - k, g, b - k, a)
    box = out.getchannel('A').point(lambda v: 255 if v > 40 else 0).getbbox()
    bag = out.crop(box)
    bag = bag.resize((round(bag.width * 420 / bag.height), 420), Image.LANCZOS)
    bag.save(D + name + '.png', optimize=True)
    bag.save(D + name + '.webp', quality=90, method=6)
    print(name, bag.size, 'from', box)

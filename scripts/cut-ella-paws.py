"""Ella's two paws on the umbrella she holds out (user pick 2026-11-26, idea 4: the umbrella glows and grows a little
under her paws): the paws cut from assets/characters/ella-give.webp into a layer the size of the umbrella's tap box
(hold.artBox in index.html, 24,362 - 591,488), laid over the growing umbrella so the paws stay put and keep holding it.
Writes assets/characters/ella-give-paws.webp.

Run: python -I scripts/cut-ella-paws.py   (Pillow only)
"""
from PIL import Image, ImageFilter
D = 'assets/characters/'
E = Image.open(D + 'ella-give.webp').convert('RGBA')
BOX = (24, 362, 591, 488)
# where each paw is in the sprite (px), a little roomy, and a point inside it
PAWS = [((146, 410, 212, 472), (180, 440)), ((408, 410, 476, 472), (440, 440))]
src = E.crop(BOX); p = src.load()
m = Image.new('L', src.size, 0); mp = m.load()
def paw_ink(c):
    r, g, b, a = c
    # the paw's brown (red a little over green, green about blue) and its dark outline; not the cardigan's orange
    return a > 100 and r < 150 and 18 < r - g < 75 and abs(g - b) < 30 or a > 100 and r < 85 and g < 60 and b < 60
for (x0, y0, x1, y1), (sx, sy) in PAWS:
    # the paw is the brown patch round its middle: grown out from there, never past its box
    todo, seen = [(sx - BOX[0], sy - BOX[1])], set()
    while todo:
        x, y = todo.pop()
        if (x, y) in seen or not (x0 - BOX[0] <= x < x1 - BOX[0] and y0 - BOX[1] <= y < y1 - BOX[1]): continue
        seen.add((x, y))
        if not paw_ink(p[x, y]): continue
        mp[x, y] = 255
        todo += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
# only the paw's own round shape: the outline lines running on into the cardigan are dropped
from PIL import ImageDraw
oval = Image.new('L', src.size, 0); d = ImageDraw.Draw(oval)
for cx, cy in ((183, 437), (441, 437)):
    d.ellipse((cx - 31 - BOX[0], cy - 24 - BOX[1], cx + 31 - BOX[0], cy + 22 - BOX[1]), fill=255)
from PIL import ImageChops
m = ImageChops.multiply(m, oval)
# fill pin holes, take in the outline round it, then soften the edge
m = m.filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.GaussianBlur(.6))
out = Image.new('RGBA', src.size)
out.paste(src, (0, 0), m)
out.save(D + 'ella-give-paws.webp', quality=92, method=6)
print('paws', out.size, out.getchannel('A').getbbox())

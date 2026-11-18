"""Case card covers made from the game's own pictures (no Higgsfield; user request 2026-11-19):
- assets/places/kite/kite-cover.jpg: the kite case's park as it is now (park.webp) with its kites where the case hides
  them (KITE_SLOTS in index.html: three in the trees under leaf clumps, one under the ball, one on the path; the flower
  bed with its bunches; the one in the bed left hidden)
- assets/places/montage/cover.jpg: the robbery case's wanted poster with the bear's face kept secret (user sketch: the
  bear's outline hatched over, a question mark on the face), so the card does not give the answer away. The bear's
  outline is the montage's blank bear (assets/montage/src/base2-higgsfield-original.png).
Run from the project folder: python -I scripts/make-case-covers.py"""
import math
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

# ---------- the kite case ----------
K = 'assets/places/kite/'
park = Image.open(K + 'park.webp').convert('RGBA')
KITE_K = 110 / 426
KITE_PICS = {1: (425, 1082), 2: (425, 1084), 3: (425, 691), 4: (425, 1082), 5: (441, 1080), 6: (318, 1082)}
KITE_CLUMPS = {'leafclump-1': (422, 262), 'leafclump-2': (267, 289), 'leafclump-3': (304, 337), 'leafclump-4': (227, 411)}
KITE_FLOWERS = [(231, 169), (200, 155), (219, 153), (211, 159), (206, 154), (209, 155)]
KITE_BED, BUNCH_H = 552, 54

def put(img, src, x, y, w, h):
    img.alpha_composite(Image.open(src).convert('RGBA').resize((round(w), round(h)), Image.LANCZOS), (round(x), round(y)))

def kite(img, n, x, y, r, s=1):
    """kite n, its top middle at (x, y), turned r degrees (clockwise) round (x, y + 20), as the game draws it"""
    w, h = KITE_PICS[n]; k = KITE_K * s
    layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
    put(layer, f'{K}kite2-{n}.png', x - w * k / 2, y, w * k, h * k)
    img.alpha_composite(layer.rotate(-r, center=(x, y + 20), resample=Image.BICUBIC))

def clump(img, name, x, y, w, h):
    pw, ph = KITE_CLUMPS[name]; sc = math.sqrt(w * h * 1.3 / (pw * ph)); W, H = pw * sc, ph * sc
    put(img, f'{K}{name}.png', x + w / 2 - W / 2, y + h / 2 - H / 2, W, H)

def bunch(img, cx, i, seed):
    f = (i * 5 + seed) % 6; fw, fh = KITE_FLOWERS[f]
    bh = BUNCH_H * (.92 + ((i * 7 + seed) % 4) * .04); bw = fw * bh / fh
    put(img, f'{K}flower-{f + 1}.png', cx - bw / 2, KITE_BED + 2 - bh, bw, bh)

for n, x, y, r, s in ((4, 150, 60, -8, 1), (2, 385, 95, 6, 1), (5, 1110, 35, -6, 1), (6, 930, 615, -80, 1), (3, 633, 670, 84, .6)):
    kite(park, n, x, y, r, s)
for args in (('leafclump-2', 52, 38, 136, 137), ('leafclump-3', 112, 48, 136, 133), ('leafclump-1', 287, 73, 136, 137),
             ('leafclump-2', 347, 83, 136, 133), ('leafclump-3', 1012, 13, 136, 137), ('leafclump-4', 1072, 23, 136, 133)):
    clump(park, *args)
for i, d in enumerate([-82, -50, -20, 20, 50, 82]): bunch(park, 560 + d, i, 1)
for i in range(7): bunch(park, 672 + i * 38, i, 4)
put(park, 'assets/props/ball-soccer.png', 628 - 42, 690 - 42, 84, 84)
park.convert('RGB').resize((688, 384), Image.LANCZOS).save(K + 'kite-cover.jpg', quality=88)

# ---------- the robbery case ----------
M = 'assets/places/montage/'
poster = Image.open(M + 'wanted.jpg').convert('RGB')
# the bear off the poster: each row the colour of the paper in its left margin, with a little grain, fading into the
# paper round it (tiled paper showed stripes)
import random
random.seed(3)
strip = poster.crop((28, 232, 108, 1008)).resize((1, 776), Image.BOX).resize((700, 776))
grain = Image.effect_noise((700, 776), 6).convert('RGB')
paper = ImageChops.add(strip, grain, 1, -128)
fade = Image.new('L', (700, 776), 0); ImageDraw.Draw(fade).rectangle((14, 6, 686, 776), fill=255)
poster.paste(paper, (100, 232), fade.filter(ImageFilter.GaussianBlur(8)))
# the bear's outline: the blank bear, its paper away (followed in from the top and the sides, not from the bottom
# where the shirt meets the edge)
b = Image.open('assets/montage/src/base2-higgsfield-original.png').convert('RGB')
bg = b.getpixel((8, 8))
d = ImageChops.difference(b, Image.new('RGB', b.size, bg)).convert('L').point(lambda v: 255 if v * 3 > 26 else 0)
W, H = b.size
for x in range(0, W, 16):
    if d.getpixel((x, 0)) == 0: ImageDraw.floodfill(d, (x, 0), 128)
for y in range(0, H - 40, 16):
    for x in (0, W - 1):
        if d.getpixel((x, y)) == 0: ImageDraw.floodfill(d, (x, y), 128)
shape = d.point(lambda v: 0 if v == 128 else 255).filter(ImageFilter.MedianFilter(9))
k = .38; shape = shape.resize((round(W * k), round(H * k)), Image.LANCZOS)
ox, oy = 432 - round(900 * k), 330 - round(495 * k)
mask = Image.new('L', poster.size, 0); mask.paste(shape, (ox, oy))
# hatched over in pen, as the user's sketch: a dark outline, diagonal strokes inside
ink = (74, 54, 40)
hatch = Image.new('RGB', poster.size, (196, 160, 122)); hd = ImageDraw.Draw(hatch)
for i in range(-poster.height, poster.width, 16): hd.line([(i, poster.height), (i + poster.height * .9, 0)], fill=ink, width=5)
poster.paste(hatch, (0, 0), mask)
edge = ImageChops.subtract(mask.filter(ImageFilter.MaxFilter(9)), mask)
poster.paste(Image.new('RGB', poster.size, ink), (0, 0), edge)
# the question mark on the face, paper-coloured with a dark rim
font = ImageFont.truetype('C:/Windows/Fonts/NanumSquareEB.ttf', 300)
qd = ImageDraw.Draw(poster)
qd.text((432, 610), '?', font=font, anchor='mm', fill=(246, 236, 214), stroke_width=12, stroke_fill=ink)
poster.save(M + 'cover.jpg', quality=88)
print('kite-cover', park.size, '-> 688x384; montage cover', poster.size)

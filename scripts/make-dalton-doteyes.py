"""Dalton's dot eyes (user request 2026-11-23: the white eyes looked scary; all poses get plain dot eyes, as the default
pose and the wave had). Credit-free, after one Higgsfield edit of the four-pose sheet:
  dalton-poses-doteyes-higgsfield-original.png  (Nano Banana 2.1 edit of dalton-poses-higgsfield-original.png,
      job 338b1ba7-9559-4d52-b1f3-e5f59fa1b571): the pointing and lens poses got dot eyes, the thinking pose kept white eyes.
This script takes the background-removed sheet dalton-poses-cutout.png and
  - pastes the new dot eyes of the pointing and lens poses in from the edited sheet (soft round patches over the face),
  - covers the thinking pose's white eyes with fur colour and draws dot eyes there (glancing up, as before),
and writes dalton-poses-doteyes-cutout.png, which scripts/cut-dalton-terry.py then cuts.
Run: python -I scripts/make-dalton-doteyes.py ; python -I scripts/cut-dalton-terry.py   (fix-dalton-eyes.py no longer runs)"""
from PIL import Image, ImageDraw, ImageFilter
import random
D = 'assets/characters/'
cut = Image.open(D + 'dalton-poses-cutout.png').convert('RGBA')
new = Image.open(D + 'dalton-poses-doteyes-higgsfield-original.png').convert('RGBA')

def soft_disc(size, cx, cy, r0, r1):
    """mask: 255 inside r0, fading to 0 at r1"""
    m = Image.new('L', size, 0); d = ImageDraw.Draw(m)
    steps = 12
    for i in range(steps, -1, -1):
        r = r0 + (r1 - r0) * i / steps
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=round(255 * (1 - i / steps)))
    return m

# 1) pointing and lens: the edited sheet's eyes (sheet px: centre, inner radius, outer radius)
PATCH = [(984, 562, 40, 50), (1148, 556, 40, 50),      # pointing
         (1612, 565, 36, 45), (1790, 560, 40, 50)]     # lens: inside the magnifier, the other eye
for cx, cy, r0, r1 in PATCH:
    m = soft_disc(cut.size, cx, cy, r0, r1)
    rgb = new.copy(); rgb.putalpha(cut.getchannel('A'))   # keep the cutout's outline
    cut = Image.composite(rgb, cut, m)

# 2) thinking: fur over the white eyes, then dot eyes looking up
EYES = [(320, 560), (490, 555)]
px = cut.load(); rnd = random.Random(7)
def fur_colour(cx, cy):
    cols = []
    for y in range(cy - 50, cy + 50):
        for x in range(cx - 50, cx + 50):
            d2 = (x - cx) ** 2 + (y - cy) ** 2
            if 41 ** 2 <= d2 <= 49 ** 2:
                p = px[x, y]
                if p[3] > 240 and p[0] > 200 and 90 < p[1] < 150 and p[2] < 90: cols.append(p)  # orange fur only
    cols.sort(key=lambda p: sum(p[:3])); mid = cols[len(cols) // 2]
    return mid, cols
for i, (cx, cy) in enumerate(EYES):
    mid, cols = fur_colour(cx, cy)
    fill = Image.new('RGBA', cut.size, mid); fp = fill.load()
    for y in range(cy - 42, cy + 42):          # crayon grain: fur pixels sampled from the ring around
        for x in range(cx - 42, cx + 42):
            fp[x, y] = rnd.choice(cols)
    fill = fill.filter(ImageFilter.GaussianBlur(.6))
    cut = Image.composite(fill, cut, soft_disc(cut.size, cx, cy, 36, 41))

K = 4; INK = (58, 27, 24, 255)
def dot(seed, w=33, h=47):
    rnd = random.Random(seed)
    im = Image.new('RGBA', (w * K, h * K)); d = ImageDraw.Draw(im)
    d.ellipse((0, 0, w * K - 1, h * K - 1), fill=INK)
    p = im.load()                               # a little crayon grain at the edge
    for _ in range(w * h * 2):
        x, y = rnd.randrange(w * K), rnd.randrange(h * K)
        if p[x, y][3] and ((x / (w * K) - .5) ** 2 + (y / (h * K) - .5) ** 2) > .2: p[x, y] = (78, 40, 34, 255)
    return im.resize((w, h), Image.LANCZOS)
for i, (cx, cy) in enumerate(EYES):
    e = dot(i); ex, ey = cx + 3, cy - 8          # glancing up and a little to the right, as the drawn pupils did
    cut.alpha_composite(e, (round(ex - e.width / 2), round(ey - e.height / 2)))

cut.save(D + 'dalton-poses-doteyes-cutout.png', optimize=True)
print('dalton-poses-doteyes-cutout.png written')

"""The accident scene's picture put right by hand (the twins case, 2026-11-25, 0 credits): the drawing had the reference's
cobblestones along the bottom and skid marks turning round like a U. The marks are taken off and drawn again along the
road (a sudden stop), and the road goes on plain to the bottom edge.
road-higgsfield-original.png -> road-fixed.png, which cut-twins-places.py cuts.
Run from the project folder: python -I scripts/fix-twins-road.py"""
import math, random
from PIL import Image, ImageChops, ImageDraw, ImageFilter
D = 'assets/places/twins/'
im = Image.open(D + 'road-higgsfield-original.png').convert('RGB')
im = im.resize((1376, round(im.height * 1376 / im.width)), Image.LANCZOS)
W, H = im.size
R = random.Random(7)


def noise(w, h, gx, gy, amp, blur):
    n = Image.new('L', (w // gx + 2, h // gy + 2))
    n.putdata([R.randint(128 - amp, 128 + amp) for _ in range(n.width * n.height)])
    return n.resize((w, h), Image.BICUBIC).filter(ImageFilter.GaussianBlur(blur))


def add(img, n):   # n around 128
    return ImageChops.add(img, Image.merge('RGB', (n, n, n)), 1, -128)


# 1. the road goes on plain from LINE down: its own colour there, a little darker towards the viewer, with brush texture
LINE, FADE = 1440, 90
strip = im.crop((300, LINE - 130, 700, LINE - 40)).resize((1, 1), Image.BOX).getpixel((0, 0))
near = (228, 204, 178)
low = Image.new('RGB', (1, H - LINE + FADE))
for y in range(low.height):
    t = max(0, (y - FADE) / (H - LINE)) * .4
    low.putpixel((0, y), tuple(round(a * (1 - t) + b * t) for a, b in zip(strip, near)))
low = add(add(low.resize((W, H - LINE + FADE)), noise(W, H - LINE + FADE, 60, 8, 4, 6)), noise(W, H - LINE + FADE, 3, 3, 2, 1))
ramp = Image.new('L', (1, low.height), 255)
for y in range(FADE):
    ramp.putpixel((0, y), round(255 * y / FADE))
im.paste(low, (0, LINE - FADE), ramp.resize((W, low.height)))

# 2. the old skid marks off: their dark pixels (and what is round them), filled with the road beside them, row by row
X0, Y0, Y1 = 740, 972, 1365
mask = Image.new('L', (W, H), 0)
mp, px = mask.load(), im.load()
for y in range(Y0, Y1):
    for x in range(X0, W):
        if (x > 1120 and y < 1135) or (y < 980 and x > 860):   # the pole, the tape, its shadow; the cones' feet
            continue
        r, g, b = px[x, y]
        if r < 226 or g < 206:
            mp[x, y] = 255
wide = mask.filter(ImageFilter.MaxFilter(19))
wp = wide.load()
fill = Image.new('RGB', (1, H))
last = strip
for y in range(Y0 - 10, Y1 + 30):
    row = [px[x, y] for x in range(X0 - 160, W, 3) if not wp[x, y] and px[x, y][0] > 232]
    if row:
        last = tuple(sorted(c[i] for c in row)[len(row) // 2] for i in range(3))
    fill.putpixel((0, y), last)
fill = fill.crop((0, Y0 - 10, 1, Y1 + 30)).filter(ImageFilter.BoxBlur(12)).resize((W, Y1 + 40 - Y0))
fill = add(add(fill, noise(W, fill.height, 60, 8, 4, 5)), noise(W, fill.height, 3, 3, 3, 1))
clean = im.copy(); clean.paste(fill, (0, Y0 - 10))
soft = wide.filter(ImageFilter.GaussianBlur(4))
im = Image.composite(clean, im, soft)

# 3. the new ones: two marks along the road, far to near, wider and further apart as they come, in pencil streaks; they
# end suddenly
S = 3
lay = Image.new('RGBA', (W * S, H * S), (0, 0, 0, 0))
d = ImageDraw.Draw(lay)


def mark(p, q, w0, w1):
    n, k = 60, 30
    for j in range(k):
        u = j / (k - 1) - .5
        start, stop = R.uniform(0, .2) + abs(u) * .3, R.uniform(.95, 1)
        pts = []
        for i in range(n + 1):
            t = i / n
            if start <= t <= stop:
                w = w0 + (w1 - w0) * t
                pts.append(((p[0] + (q[0] - p[0]) * t + 16 * math.sin(t * 2.4) + u * w) * S, (p[1] + (q[1] - p[1]) * t) * S))
        g = R.randint(66, 96)
        d.line(pts, fill=(g, g - 6, g - 10, R.randint(110, 180)), width=max(2, round((w0 + w1) / 2 / k * S * 1.1)), joint='curve')


mark((850, 990), (800, 1400), 12, 40)
mark((960, 990), (1050, 1400), 12, 40)
im = im.convert('RGBA')
im.alpha_composite(lay.resize((W, H), Image.LANCZOS))
im.convert('RGB').save(D + 'road-fixed.png')
print(im.size, strip)

"""Kite case: the leaf clumps that hide the kites in the park's trees (user requests 2026-11-18: the kites not in plain
sight; the clumps natural, not stamped clouds with an outline). One clump per cover of each tree kite in KITE_SLOTS
(index.html): cut from the full-size park band (park-hi.webp) a little above where it sits, so its leaves are that
tree's own colour, a lumpy mass of round lobes with a soft edge, a touch darker and fuller than the crown behind it,
and a faint shadow under it -> assets/places/kite/cover-<n>-<i>.png (the cover box at the band's full size, plus the
shadow's margin; drawn over the box with that margin, see kitesArt).
Run from the project folder: python -I scripts/make-kite-leaves.py"""
import re, random
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageChops
D = 'assets/places/kite/'
hi = Image.open(D + 'park-hi.webp').convert('RGB')
F = hi.width / 1376          # band px -> full-size px
PAD = 10                     # band px around the box for the soft edge and the shadow (kitesArt draws it the same)
html = open('index.html', encoding='utf8').read()
slots = re.findall(r"\{ n:(\d), at:'tree'.*?cover:\[(.*?)\] \}", html)
for n, covers in slots:
    for i, (img, x, y, w, h) in enumerate(re.findall(r"\['([\w-]+)', (\d+), (\d+), (\d+), (\d+)\]", covers)):
        x, y, w, h = int(x), int(y), int(w), int(h)
        W, H = round((w + 2 * PAD) * F), round((h + 2 * PAD) * F)
        sx, sy = round((x - PAD) * F), max(0, round((y - PAD - h * .35) * F))
        tex = hi.crop((sx, sy, sx + W, sy + H))
        tex = ImageEnhance.Brightness(ImageEnhance.Color(tex).enhance(1.12)).enhance(.93)
        random.seed(int(n) * 10 + i)
        m = Image.new('L', (W, H), 0); d = ImageDraw.Draw(m)
        p = PAD * F
        d.ellipse((p + W * .05, p + H * .12, W - p - W * .05, H - p - H * .05), fill=255)
        for k in range(10):
            r = random.uniform(.16, .24) * min(W, H)
            cx = random.uniform(p + r * .8, W - p - r * .8); cy = random.uniform(p + r * .8, H - p - r * .8)
            d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=255)
        m = m.filter(ImageFilter.GaussianBlur(3.5 * F))
        shadow = ImageChops.offset(m, 0, round(5 * F)).filter(ImageFilter.GaussianBlur(5 * F)).point(lambda v: v * 70 // 255)
        out = Image.new('RGBA', (W, H), (40, 60, 25, 0)); out.putalpha(shadow)
        leaf = Image.new('RGBA', (W, H)); leaf.paste(tex, (0, 0), m)
        out.alpha_composite(leaf)
        out.save(D + f'cover-{n}-{i}.png', optimize=True)
        print(f'cover-{n}-{i}', out.size)

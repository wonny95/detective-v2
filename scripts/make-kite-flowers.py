"""Kite case: flower clumps that hide the two kites in the flower bed (user request 2026-11-18: not every kite in the
trees). Cut from the flower bed of the full-size park band (park-hi.webp, scripts/cut-kite-places.py), a mound of
round lobes with a soft edge, no outline (the flowers have none) -> assets/places/kite/flowers-1..2.png (280x140, drawn at 130x66).
Run from the project folder: python -I scripts/make-kite-flowers.py"""
import random
from PIL import Image, ImageDraw, ImageFilter
D = 'assets/places/kite/'
hi = Image.open(D + 'park-hi.webp').convert('RGB')
random.seed(3)
for n, (sx, sy) in enumerate([(610, 598), (890, 598)], 1):
    W, H = 280, 140
    tex = hi.crop((sx, sy, sx + W, sy + H))
    m = Image.new('L', (W, H), 0); d = ImageDraw.Draw(m)
    # a mound of round lobes, every edge soft (a straight edge showed as a seam in the close look)
    d.ellipse((24, 34, W - 24, H - 14), fill=255)
    for i in range(8):
        cx = 40 + i * 28 + random.randint(-6, 6); cy = 52 + random.randint(-12, 22); r = random.randint(26, 34)
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=255)
    m = m.filter(ImageFilter.GaussianBlur(5))
    out = Image.new('RGBA', (W, H)); out.paste(tex, (0, 0), m); out.save(D + f'flowers-{n}.png', optimize=True)
    print('flowers', n)

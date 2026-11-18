"""Kite case: the flower bunches that hide a kite in the flower bed and part to the sides when tapped (user request
2026-11-18, with sketches: the flowers are pushed aside, not cleared away, and stand back once the kite is taken).
One Higgsfield sheet on flat magenta drawn with the park's flower bed as its reference (flowers-sheet-original.png,
job 707c9fc0): six short bushy clumps, a mound of leaves with flowers on short stems (user: the first, tall bunches
with long stems, flowers-sheet-tall-original.png job 091ba324, looked creepy) -> flower-1..6.png, magenta keyed out with
despill, each cut to itself + 4 px (the base at the bottom edge, where it is turned from; kitesArt).
Prints each size. Run from the project folder: python -I scripts/cut-kite-flower-sheet.py"""
from PIL import Image
D = 'assets/places/kite/'
src = Image.open(D + 'flowers-sheet-original.png').convert('RGB')
W, H = src.size
px = src.load(); out = Image.new('RGBA', src.size); op = out.load()
for y in range(H):
    for x in range(W):
        r, g, b = px[x, y]; mag = min(r, b) - g
        a = 255 if mag < 60 else max(0, 255 - int((mag - 60) * 255 / 70))
        if a < 255 and mag > 0:
            k = min(r, b) - (g + 25)
            if k > 0: r, b = r - k, b - k
        op[x, y] = (r, g, b, a)
A = out.getchannel('A').point(lambda v: 255 if v > 60 else 0)
cols, x, n = [], 0, 0
on = [any(A.getpixel((x, y)) for y in range(0, H, 3)) for x in range(W)]
while x < W:
    if on[x]:
        s = x
        while x < W and on[x]: x += 1
        if x - s > 30: cols.append((s, x))
    x += 1
for n, (x0, x1) in enumerate(cols, 1):
    part = out.crop((x0, 0, x1, H)); bb = A.crop((x0, 0, x1, H)).getbbox()
    part = part.crop((max(bb[0] - 4, 0), max(bb[1] - 4, 0), min(bb[2] + 4, part.width), bb[3]))
    part.save(D + f'flower-{n}.png', optimize=True); print(f'flower-{n}', part.size)

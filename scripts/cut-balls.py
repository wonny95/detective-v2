"""Balls for any case (user request 2026-11-18: several balls in the game's style on one sheet, to use later; the soccer
ball hides a kite in the kite case's park). One Higgsfield sheet on flat magenta drawn after the park picture
(assets/props/balls-sheet-original.png, job 9bbdab26): four large balls on top, four small below ->
assets/props/ball-<name>.png, magenta keyed out with despill, each cut to itself + 4 px.
Prints each size. Run from the project folder: python -I scripts/cut-balls.py"""
from PIL import Image
D = 'assets/props/'
NAMES = [['soccer', 'beach', 'basket', 'rubber'], ['tennis', 'baseball', 'volley', 'bouncy']]
src = Image.open(D + 'balls-sheet-original.png').convert('RGB')
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
def runs(vals, minlen):
    rs, i = [], 0
    while i < len(vals):
        if vals[i]:
            s = i
            while i < len(vals) and vals[i]: i += 1
            if i - s >= minlen: rs.append((s, i))
        i += 1
    return rs
rows = runs([any(A.getpixel((x, y)) for x in range(0, W, 3)) for y in range(H)], 30)
for (y0, y1), names in zip(rows, NAMES):
    band = A.crop((0, y0, W, y1))
    cols = runs([any(band.getpixel((x, y)) for y in range(0, y1 - y0, 3)) for x in range(W)], 30)
    for (x0, x1), name in zip(cols, names):
        part = out.crop((x0, y0, x1, y1)); bb = A.crop((x0, y0, x1, y1)).getbbox()
        part = part.crop((max(bb[0] - 4, 0), max(bb[1] - 4, 0), min(bb[2] + 4, part.width), min(bb[3] + 4, part.height)))
        part.save(D + f'ball-{name}.png', optimize=True); print(f'ball-{name}', part.size)

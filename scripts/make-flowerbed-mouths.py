"""Talking mouths for the flowerbed case (user request 2026-11-23): Ollie (otter), Gus (raccoon, also his sorry face) and
Pablo (panda). Sheet: mouths/flowerbed-sheet-higgsfield-original.png (Nano Banana 2.1 16:9 1K, job
7ef8bc68-a4af-4916-a4ba-7d17b4aa7f5f, the Ollie/Gus and Pablo pictures as reference, flat green): three columns
otter / raccoon / panda, top row closed, bottom row open, each on a round patch of that fur.

closed = the picture as drawn (a crop of the sprite). open = the drawn mouth painted over with the fur around it
(median colour, feathered ellipse) and the sheet's open mouth on top (Gus's sorry face takes the otter's worried open
mouth, which fits a sad face). As scripts/make-dalton-terry-mouths.py. Writes mouths/<name>-closed|open.png/.webp
and prints the MOUTHS boxes.
Run: python -I scripts/cut-gus-moods.py ; python -I scripts/make-flowerbed-mouths.py   (Pillow only)"""
from PIL import Image, ImageDraw, ImageFilter
import statistics, math
D = 'assets/characters/'; M = D + 'mouths/'
sheet = Image.open(M + 'flowerbed-sheet-higgsfield-original.png').convert('RGB')
COL = {'otter': 268, 'raccoon': 672, 'panda': 1075}; ROW = {'closed': 200, 'open': 555}; R = 150
def mouth_art(kind, state):
    """the mouth alone (fur keyed out) from one sheet cell, cropped to it"""
    cx, cy = COL[kind], ROW[state]
    cell = sheet.crop((cx - R, cy - R, cx + R, cy + R)); px = cell.load()
    ring = [px[round(R + .75 * R * math.cos(a)), round(R + .75 * R * math.sin(a))] for a in [i * math.pi / 18 for i in range(18, 36)]]  # upper half
    fur = tuple(statistics.median(c[i] for c in ring) for i in range(3))
    a = Image.new('L', cell.size); ap = a.load()
    for y in range(cell.height):
        for x in range(cell.width):
            if (x - R) ** 2 + (y - R) ** 2 > (R - 14) ** 2: continue
            d = sum(abs(px[x, y][i] - fur[i]) for i in range(3))
            ap[x, y] = int(max(0, min(255, (d - 70) * 3)))
    out = cell.convert('RGBA'); out.putalpha(a)
    return out.crop(a.point(lambda v: 255 if v > 200 else 0).filter(ImageFilter.MinFilter(5)).getbbox())
def cover(sprite, box):
    """paint the drawn mouth over with the fur around it: (x0, y0, x1, y1) ellipse, feathered"""
    x0, y0, x1, y1 = box; px = sprite.load(); ring = []
    for x in range(x0 - 4, x1 + 5, 2):
        for y in (y0 - 5, y1 + 5): ring.append(px[x, y])
    fur = tuple(int(statistics.median(c[i] for c in ring)) for i in range(3)) + (255,)
    m = Image.new('L', sprite.size); ImageDraw.Draw(m).ellipse(box, fill=255); m = m.filter(ImageFilter.GaussianBlur(2))
    sprite.paste(Image.new('RGBA', sprite.size, fur), (0, 0), m)
# name: (sprite file, open mouth kind, drawn mouth ellipse to cover (sprite px), open mouth centre x, top y, width)
P = {'ollie': ('ollie-higgsfield', 'otter', (288, 221, 360, 245), 324, 222, 58),
     'gus': ('gus-higgsfield', 'raccoon', (178, 254, 254, 286), 206, 256, 58),
     'gus-sorry': ('gus-sorry', 'otter', (160, 259, 254, 288), 206, 262, 56),
     'pablo': ('pablo-higgsfield', 'panda', (154, 214, 245, 242), 200, 218, 66)}
for name, (src, kind, cbox, cx, top, ow) in P.items():
    spr = Image.open(D + f'{src}.png').convert('RGBA')
    op = mouth_art(kind, 'open'); op = op.resize((ow, round(op.height * ow / op.width)), Image.LANCZOS)
    x0 = min(cbox[0], cx - ow // 2) - 4; y0 = min(cbox[1], top) - 4
    x1 = max(cbox[2], cx + ow // 2) + 4; y1 = max(cbox[3], top + op.height) + 4
    closed = spr.crop((x0, y0, x1, y1))
    o = spr.copy(); cover(o, cbox); o.alpha_composite(op, (cx - ow // 2, top)); opened = o.crop((x0, y0, x1, y1))
    for st, im in (('closed', closed), ('open', opened)):
        im.save(M + f'{name}-{st}.png', optimize=True); im.save(M + f'{name}-{st}.webp', quality=92, method=6)
    w, h = x1 - x0, y1 - y0
    print(f"  '{name.replace('-', ':', 1)}':{{closed:[{x0},{y0},{w},{h}], open:[{x0},{y0},{w},{h}]}},")

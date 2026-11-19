"""Talking mouths for Dalton's five poses and Terry (user request 2026-11-19: one Higgsfield sheet, like the NPC mouths).
Sheet: mouths/dalton-terry-sheet-higgsfield-original.png (job 09dddce9-…, 1376x768, flat green): top row the mouse's
closed / open mouth on orange fur, bottom row the cat's on white fur.

closed = the picture as drawn (a crop of the sprite), except the wave pose, whose drawn mouth is open: there the sheet's
closed smile goes on a cover. open = the drawn mouth painted over with the fur around it (flat median colour, feathered
ellipse) and the sheet's open mouth on top. Writes mouths/<name>-closed|open.png/.webp and prints MOUTHS boxes.
Run: python -I scripts/make-dalton-terry-mouths.py   (Pillow only)"""
from PIL import Image, ImageDraw, ImageFilter
import statistics
D = 'assets/characters/'; M = D + 'mouths/'
sheet = Image.open(M + 'dalton-terry-sheet-higgsfield-original.png').convert('RGB')
CELLS = {('mouse', 'closed'): (345, 200), ('mouse', 'open'): (1023, 205), ('cat', 'closed'): (345, 560), ('cat', 'open'): (1023, 560)}
def mouth_art(kind, state):
    """the mouth alone (fur keyed out) from one sheet cell, cropped to it"""
    cx, cy = CELLS[kind, state]; r = 92
    cell = sheet.crop((cx - r, cy - r, cx + r, cy + r))
    px = cell.load(); fur = [px[x, y] for x in range(30, 2 * r - 30, 7) for y in (40, 2 * r - 40)]
    fur = tuple(statistics.median(c[i] for c in fur) for i in range(3))
    a = Image.new('L', cell.size); ap = a.load()
    for y in range(cell.height):
        for x in range(cell.width):
            if (x - r) ** 2 + (y - r) ** 2 > (r - 6) ** 2: continue
            d = sum(abs(px[x, y][i] - fur[i]) for i in range(3))
            ap[x, y] = int(max(0, min(255, (d - 60) * 3)))
    out = cell.convert('RGBA'); out.putalpha(a)
    return out.crop(a.point(lambda v: 255 if v > 200 else 0).filter(ImageFilter.MinFilter(5)).getbbox())
def cover(sprite, box):
    """paint the drawn mouth over with the fur around it: (x0, y0, x1, y1) ellipse, feathered"""
    x0, y0, x1, y1 = box; px = sprite.load(); ring = []
    for x in range(x0 - 6, x1 + 7, 2):
        for y in (y0 - 6, y1 + 6): ring.append(px[x, y])
    fur = tuple(int(statistics.median(c[i] for c in ring)) for i in range(3)) + (255,)
    m = Image.new('L', sprite.size); ImageDraw.Draw(m).ellipse(box, fill=255); m = m.filter(ImageFilter.GaussianBlur(2))
    sprite.paste(Image.new('RGBA', sprite.size, fur), (0, 0), m)
# name: (kind, drawn mouth ellipse to cover (sprite px), mouth centre x, mouth top y, open mouth width, closed width or None)
P = {'dalton': ('mouse', (245, 297, 283, 319), 264, 300, 30, None),
     'dalton-thinking': ('mouse', (212, 287, 250, 302), 231, 284, 24, None),
     'dalton-point': ('mouse', (205, 280, 246, 302), 226, 284, 31, None),
     'dalton-lens': ('mouse', (208, 286, 243, 303), 225, 288, 28, None),
     'dalton-wave': ('mouse', (186, 280, 252, 319), 219, 288, 32, 30),
     'terry': ('cat', (182, 263, 262, 287), 222, 268, 40, None)}
for name, (kind, cbox, cx, top, ow, cw) in P.items():
    spr = Image.open(D + f'{name}.png').convert('RGBA')
    op = mouth_art(kind, 'open'); op = op.resize((ow, round(op.height * ow / op.width)), Image.LANCZOS)
    x0 = min(cbox[0], cx - ow // 2) - 4; y0 = min(cbox[1], top) - 4
    x1 = max(cbox[2], cx + ow // 2) + 4; y1 = max(cbox[3], top + op.height) + 4
    if cw:   # the drawn mouth is open: closed = cover + the sheet's closed smile
        cl = mouth_art(kind, 'closed'); cl = cl.resize((cw, round(cl.height * cw / cl.width)), Image.LANCZOS)
        c = spr.copy(); cover(c, cbox); c.alpha_composite(cl, (cx - cw // 2, top + 6)); closed = c.crop((x0, y0, x1, y1))
    else: closed = spr.crop((x0, y0, x1, y1))
    o = spr.copy(); cover(o, cbox); o.alpha_composite(op, (cx - ow // 2, top)); opened = o.crop((x0, y0, x1, y1))
    for st, im in (('closed', closed), ('open', opened)):
        im.save(M + f'{name}-{st}.png', optimize=True); im.save(M + f'{name}-{st}.webp', quality=92, method=6)
    w, h = x1 - x0, y1 - y0
    print(f"  '{name.replace('-', ':', 1)}':{{closed:[{x0},{y0},{w},{h}], open:[{x0},{y0},{w},{h}]}},")

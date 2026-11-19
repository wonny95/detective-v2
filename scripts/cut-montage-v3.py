"""The robbery case's montage, third set (2026-11-19, user plan: no overlapping mouth, ears or clothes):
- base3 (Higgsfield nano_banana_2, job b5e9c574): base2 with the ears, the closed smile and the body taken away; only
  the head is cut from it (a faint shirt was left in the picture) -> assets/montage/head.webp, same frame as before, so
  the eyes, teeth, cap and scar of the second set (scripts/cut-montage-parts.py) still sit on it
- vest3 (job 4c92a10b, a 2x3 sheet, the last cell empty): the bear's body in each vest (none, one, jacket, two, three);
  the vest brings the body (Betty says the vest first). A bust in the face's frame, as before (BODY, SQUASH below).
- ears3 (job 4b034916): five pairs of ears, each pair whole (the head has none)
- scarf3 (job 67ef5dd2): five scarves of one shape, narrow round the neck so the chest pockets show
Run from the project folder: python -I scripts/cut-montage-v3.py [preview <out.png>]"""
import sys
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageStat

SRC, OUT = 'assets/montage/src/', 'assets/montage/'
FRAME = (0, 160, 1792, 2400)   # the head's part of base3, as in the second set (halved: 896 x 1120)
FW, FH = 896, 1120

# ---- the head: the warm fur and lines inside an oval round it, filled in, the bit of neck under the chin dropped
b = Image.open(SRC + 'base3-higgsfield-original.png').convert('RGBA')
m = Image.new('L', b.size, 0); ImageDraw.Draw(m).ellipse((40, 420, 1752, 1880), fill=255)
r, g, bl, a = b.split()
warm = ImageChops.lighter(ImageChops.subtract(r, bl).point(lambda v: 255 if v > 45 else 0), r.point(lambda v: 255 if v < 120 else 0))
keep = ImageChops.multiply(m, warm).filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.MinFilter(9))
ImageDraw.floodfill(keep, (5, 5), 128)
keep = keep.point(lambda v: 0 if v == 128 else 255).filter(ImageFilter.GaussianBlur(1.5))
head = b.copy(); head.putalpha(keep)
head = head.crop(FRAME).resize((FW, FH), Image.LANCZOS)
ha = head.getchannel('A')
rows = [sum(1 for x in range(0, FW, 4) if ha.getpixel((x, y)) > 20) for y in range(FH)]
top = next(y for y in range(FH) if rows[y])
chin = next(y for y in range(top + 200, FH) if rows[y] == 0)
ha.paste(0, (0, chin, FW, FH)); head.putalpha(ha)
hb = ha.getbbox(); head_w = hb[2] - hb[0]

# ---- the vests: each cell of the sheet (inside its grid lines), its white paper made transparent
def cutout(im, tol=26):
    im = im.convert('RGB')
    d = ImageChops.difference(im, Image.new('RGB', im.size, (255, 255, 255))).convert('L').point(lambda v: min(255, v * 3))
    mask = d.point(lambda v: 255 if v > tol else 0)
    W, H = im.size
    for x in range(0, W, 8):
        for y in (0, H - 1):
            if mask.getpixel((x, y)) == 0: ImageDraw.floodfill(mask, (x, y), 128)
    for y in range(0, H, 8):
        for x in (0, W - 1):
            if mask.getpixel((x, y)) == 0: ImageDraw.floodfill(mask, (x, y), 128)
    out = mask.point(lambda v: 0 if v == 128 else 255)
    soft = ImageChops.lighter(out.filter(ImageFilter.MinFilter(5)), ImageChops.multiply(out, d.point(lambda v: min(255, v * 2))))
    rgba = im.convert('RGBA'); rgba.putalpha(soft)
    return rgba.crop(soft.getbbox())

sheet = Image.open(SRC + 'vest4-higgsfield-original.png').convert('RGB')
# vest4 (job 8a4151b4, user request 2026-11-19: a different garment and colours each, pockets high): the sheet drew the
# navy vest (the answer) with one chest pocket and two low ones, the mustard one with four; in the bust only the chest
# shows (to about y 590 of a cell), so they are redrawn on the chest: navy two (the right one mirrored to the left),
# mustard three (two smaller on the left, one on the right); the low ones painted over with the cloth's colour
def cloth(im, box):
    """box filled with the cloth's colour, a little grain"""
    import random
    x0, y0, x1, y1 = box
    ref = tuple(round(v) for v in ImageStat.Stat(im.crop(CLOTH)).median)
    patch = Image.new('RGB', (x1 - x0, y1 - y0), ref)
    rnd = random.Random(7); grain = Image.new('L', patch.size)
    grain.putdata([128 + rnd.randint(-14, 14) for _ in range(patch.width * patch.height)])
    grain = grain.filter(ImageFilter.GaussianBlur(1.2))
    patch = Image.merge('RGB', [ImageChops.add(c, grain, 1, -128) for c in patch.split()])
    m = Image.new('L', patch.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, patch.width - 1, patch.height - 1), 10, fill=255)
    im.paste(patch, (x0, y0), m.filter(ImageFilter.GaussianBlur(3)))
def fix(ox, oy, low, cloth_ref, moves):
    global CLOTH
    cell = sheet.crop((ox, oy, ox + 842, oy + 848))
    CLOTH = cloth_ref
    pieces = [(cell.crop(src), dst, flip) for src, dst, flip in moves]
    for box in low: cloth(cell, box)
    for piece, (x, y, w, h), flip in pieces:
        if flip: piece = piece.transpose(Image.FLIP_LEFT_RIGHT)
        m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).rounded_rectangle((3, 3, w - 4, h - 4), 8, fill=255)
        cell.paste(piece.resize((w, h), Image.LANCZOS), (x, y), m.filter(ImageFilter.GaussianBlur(2)))
    sheet.paste(cell, (ox, oy))
# navy (cell 4): low pockets out, the chest pocket again on the left (mirrored round the buttons, x 437)
fix(0, 848, [(220, 556, 355, 700), (483, 556, 618, 700)], (240, 430, 290, 540),
    [((483, 404, 589, 517), (285, 404, 106, 113), True)])
# mustard (cell 5): all four out, then two smaller on the left (stacked) and the right one where it was
fix(842, 848, [(220, 556, 362, 705), (486, 556, 630, 700), (252, 406, 382, 528)], (205, 440, 250, 540),
    [((257, 411, 376, 523), (262, 408, 98, 86), False), ((257, 411, 376, 523), (262, 500, 98, 86), False)])
SW, SH = sheet.size
sheet.save(SRC + 'vest4-fixed.png')
cells = [(c * SW // 3, r * SH // 2, (c + 1) * SW // 3, (r + 1) * SH // 2) for r in range(2) for c in range(3)]
INSET = 14   # past the grid lines
vests = {}
for oid, (x0, y0, x1, y1) in zip(['none', 'one', 'jacket', 'two', 'three'], cells):
    vests[oid] = cutout(sheet.crop((x0 + INSET, y0 + INSET, x1 - INSET, y1 - INSET)))

# a bust, as the second set (user request 2026-11-19: neck, shoulders and some chest, cut off by the frame like a
# statue's bust): the face's frame is the whole view. One scale for all (as drawn on one sheet), the body this much
# wider than the head, pressed down (SQUASH) so the pockets, which tell the vests apart, still show above the frame's
# edge; the hem goes under it
BODY = 1.32
k = head_w * BODY / vests['none'].width
NECK = 140    # the neck's top this far up under the chin
SQUASH_FIX = .7   # user pick B 2026-11-19: pressed a little, the hem well under the frame
SQUASH = SQUASH_FIX
VW, VH, OX = FW, FH, 0
print('squash', round(SQUASH, 2), 'head', hb, 'chin', chin)

def body(v):
    lay = Image.new('RGBA', (VW, VH), (0, 0, 0, 0))
    p = v.resize((round(v.width * k), round(v.height * k * SQUASH)), Image.LANCZOS)
    lay.alpha_composite(p, (VW // 2 - p.width // 2, chin - NECK))
    return lay
layers = {f'vest-{oid}': body(v) for oid, v in vests.items()}

# scarves (scarf3, job 67ef5dd2, user plan 2026-11-19: made after the vests, to sit round the bust's neck): 2x3, the
# last cell empty, all one shape; under the head (layer order), the band's top tucked under the chin
ssheet = Image.open(SRC + 'scarf3-higgsfield-original.png').convert('RGB')
scarves = {oid: cutout(ssheet.crop((x0 + INSET, y0 + INSET, x1 - INSET, y1 - INSET)))
           for oid, (x0, y0, x1, y1) in zip(['blue-dots', 'red-stripes', 'red-plain', 'green-dots', 'red-dots'], cells)}
SCARF_W, SCARF_UP = 440, 75   # its width (user request 2026-11-19: bigger, 330 looked small and mean), and how far its top goes up under the chin
ksc = SCARF_W / scarves['red-dots'].width
for oid, v in scarves.items():
    lay = Image.new('RGBA', (VW, VH), (0, 0, 0, 0))
    p = v.resize((round(v.width * ksc), round(v.height * ksc)), Image.LANCZOS)
    lay.alpha_composite(p, (VW // 2 - p.width // 2, chin - SCARF_UP))
    layers[f'scarf-{oid}'] = lay

# ears (ears3, job 4b034916): a pair in each cell (plain, torn, both bandaged, earring, one bandaged); the head has
# none, so an option always shows two. Each ear is cut from its pair at the gap and laid at base2's ear places, under
# the head (layer order), its long furry base hidden behind it. EAR_W: the round part's width, EARS: its middle.
esheet = Image.open(SRC + 'ears3-higgsfield-original.png').convert('RGB')
EAR_W, EARS = 200, ((195, 240), (701, 240))
def split_pair(p):
    a = p.getchannel('A'); prof = a.resize((a.width, 1), Image.BOX)
    mid = min(range(a.width // 3, 2 * a.width // 3), key=lambda x: prof.getpixel((x, 0)))
    return [q.crop(q.getchannel('A').getbbox()) for q in (p.crop((0, 0, mid, a.height)), p.crop((mid, 0, a.width, a.height)))]
def round_part(e):
    """the round part's width and middle: the widest row in the top half"""
    a = e.getchannel('A'); best = (0, 0, 0)
    for y in range(0, e.height // 2, 2):
        xs = [x for x in range(e.width) if a.getpixel((x, y)) > 128]
        if xs and xs[-1] - xs[0] > best[0]: best = (xs[-1] - xs[0], (xs[0] + xs[-1]) / 2, y)
    return best
for oid, (x0, y0, x1, y1) in zip(['plain', 'torn', 'both', 'earring', 'one'], cells):
    lay = Image.new('RGBA', (VW, VH), (0, 0, 0, 0))
    for e, (cx, cy) in zip(split_pair(cutout(esheet.crop((x0 + INSET, y0 + INSET, x1 - INSET, y1 - INSET)))), EARS):
        w, mx, my = round_part(e); ke = EAR_W / w
        q = e.resize((round(e.width * ke), round(e.height * ke)), Image.LANCZOS)
        lay.alpha_composite(q, (round(cx - mx * ke), round(cy - my * ke)))
    layers[f'ears-{oid}'] = lay

if 'preview' in sys.argv:
    out = sys.argv[sys.argv.index('preview') + 1]
    paper = (248, 241, 229, 255)
    def face(c, look):
        f = Image.new('RGBA', (FW, FH), (0, 0, 0, 0)); f.alpha_composite(head)
        for n in look: f.alpha_composite(Image.open(OUT + n + '.webp').convert('RGBA'))
        c.alpha_composite(f, (OX, 0)); return c
    row = Image.new('RGB', (5 * 320, 400), 'white')
    looks = [['eyes-small-thick', 'teeth-gold', 'hat-green-yellow', 'scar-above'], ['eyes-big-thin', 'teeth-plain'], [], ['eyes-sleepy-thick'], ['teeth-gap']]
    for i, oid in enumerate(['two', 'none', 'one', 'jacket', 'three']):
        c = Image.new('RGBA', (VW, VH), paper); c.alpha_composite(layers['vest-' + oid])
        c.alpha_composite(layers['scarf-' + ['red-dots', 'blue-dots', 'red-stripes', 'red-plain', 'green-dots'][i]])
        c.alpha_composite(layers['ears-' + ['one', 'plain', 'torn', 'both', 'earring'][i]]); face(c, looks[i])
        row.paste(c.convert('RGB').resize((320, 400)), (i * 320, 0))
    row.save(out); sys.exit()

head.save(OUT + 'head.webp', quality=86, method=6)
for name, img in layers.items(): img.save(OUT + name + '.webp', quality=86, method=6)
print('saved head and', len(layers), 'vests, scarves and ears')

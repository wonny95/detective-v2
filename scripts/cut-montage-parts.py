"""The robbery case's montage pictures (Case 03, design/case-03-bear-town-montage.md), cut from the Higgsfield
originals in assets/montage/src/ (2026-11-18, nano_banana_2; second set after the user's "the bear looks a mess in
play": drawn after the wanted poster, job 709ef60d, front view):
- base2 (job a1d730f8): the poster's bear with nothing distinctive (no cap, eyes, scar, bandage, scarf, vest): the frame
- eyes2 (99782805, a 3x3 sheet: five of its sets used), hat2 (8c20a936: backward caps from the front), scarf2
  (6bd11949: bandanas), vest2 (d8022a3a, 2x3: five used), ears2 (d92ef59b: single ears, laid over the base's ears)
- mouth (6cb0106a: five open grins, the teeth part: the whole mouth changes, user request), the scar from the first
  set's teeth sheet (24d0002b), darker (user: it was lost on the fur); arrows (56fc880b) were cut by the first version
Each option is laid on the base where it belongs (L, in the base picture's pixels), then every layer is saved as a
picture the size of the frame (FRAME of the base, halved), so the game only stacks them: assets/montage/<part>-<id>.webp.
An eye pair is cut and laid as one piece (the first set cut each eye alone, and they went crooked).
Run from the project folder: python -I scripts/cut-montage-parts.py [preview <out.png>]"""
import sys
from PIL import Image, ImageChops, ImageDraw, ImageFilter

SRC, OUT = 'assets/montage/src/', 'assets/montage/'
FRAME = (0, 160, 1792, 2400)   # the base's part in the frame (4:5, as the frame)
SCALE = .5

def cutout(im, tol=26):
    """the sheet's paper → transparent: the near-white connected to the border (white inside a part is kept)"""
    im = im.convert('RGB')
    bg = im.getpixel((8, 8))
    d = ImageChops.difference(im, Image.new('RGB', im.size, bg)).convert('L').point(lambda v: min(255, v * 3))
    mask = d.point(lambda v: 255 if v > tol else 0)
    W, H = im.size
    for x in range(0, W, 16):
        for y in (0, H - 1):
            if mask.getpixel((x, y)) == 0: ImageDraw.floodfill(mask, (x, y), 128)
    for y in range(0, H, 16):
        for x in (0, W - 1):
            if mask.getpixel((x, y)) == 0: ImageDraw.floodfill(mask, (x, y), 128)
    out = mask.point(lambda v: 0 if v == 128 else 255)
    edge = out.filter(ImageFilter.MinFilter(5))
    soft = ImageChops.lighter(edge, ImageChops.multiply(out, d.point(lambda v: min(255, v * 2))))
    rgba = im.convert('RGBA'); rgba.putalpha(soft)
    return rgba

def valleys(profile, n, length):
    """n parts spread evenly: cut at the emptiest place near each expected boundary"""
    cuts = [0]
    for k in range(1, n):
        e = k * length / n; r = int(length / n * .35)
        cuts.append(min(range(int(e - r), int(e + r)), key=lambda i: (profile(i), abs(i - e))))
    return cuts + [length]

def grid(rgba, rows, cols):
    """the sheet's parts, row by row, left to right, each cropped to what is in it"""
    a = rgba.getchannel('A')
    rp = a.resize((1, a.height), Image.BOX)
    out = []
    ys = valleys(lambda y: rp.getpixel((0, y)), rows, a.height)
    for y0, y1 in zip(ys, ys[1:]):
        row = a.crop((0, y0, a.width, y1)); cp = row.resize((row.width, 1), Image.BOX)
        xs = valleys(lambda x: cp.getpixel((x, 0)), cols, a.width)
        for x0, x1 in zip(xs, xs[1:]):
            p = rgba.crop((x0, y0, x1, y1)); out.append(p.crop(p.getchannel('A').getbbox()))
    return out

def place(canvas, piece, cx, cy, w, rot=0, flip=False, squash=1):
    """piece scaled to width w (its height times squash), centred on (cx, cy) in base pixels"""
    if flip: piece = piece.transpose(Image.FLIP_LEFT_RIGHT)
    p = piece.resize((round(w), round(piece.height * w / piece.width * squash)), Image.LANCZOS)
    if rot: p = p.rotate(-rot, expand=True, resample=Image.BICUBIC)
    canvas.alpha_composite(p, (round(cx - p.width / 2), round(cy - p.height / 2)))

base = Image.open(SRC + 'base2-higgsfield-original.png').convert('RGBA')
BW, BH = base.size
# the head again, over the bandana and vest: inside an oval round the head, the fur, cheeks, muzzle and lines (warm or
# dark, not the cream shirt), and all of the face above the collar
def head_of(b):
    m = Image.new('L', b.size, 0); ImageDraw.Draw(m).ellipse((180, 540, 1620, 1720), fill=255)
    r, g, bl, a = b.split()
    warm = ImageChops.lighter(ImageChops.subtract(r, bl).point(lambda v: 255 if v > 45 else 0), r.point(lambda v: 255 if v < 120 else 0))
    ImageDraw.Draw(warm).rectangle((0, 0, BW, 1560), fill=255)
    keep = ImageChops.multiply(m, warm).filter(ImageFilter.GaussianBlur(1.5))
    h = b.copy(); h.putalpha(keep); return h
head = head_of(base)
def layer(): return Image.new('RGBA', (BW, BH), (0, 0, 0, 0))
def save(img, name):
    img.crop(FRAME).resize((round((FRAME[2] - FRAME[0]) * SCALE), round((FRAME[3] - FRAME[1]) * SCALE)), Image.LANCZOS) \
       .save(OUT + name + '.webp', quality=86, method=6)

sheet = lambda n: cutout(Image.open(f'{SRC}{n}-higgsfield-original.png'))
eyes9 = grid(sheet('eyes2'), 3, 3)        # big-thin, sleepy, small-thin / sleepy, big-thick, small-thin / small-thin x2, small-thick
eyes = dict(zip(['big-thin', 'sleepy-thick', 'small-thin', '_1', 'big-thick', '_2', '_3', '_4', 'small-thick'], eyes9))
hats = grid(sheet('hat2'), 1, 5)
# the strap opening at the back of a cap is closed in by the cap, so the paper stays in it: cleared from its middle
# (user: the white in the middle of the cap)
def clear_hole(p):
    p = p.copy(); W, H = p.size
    rgb = p.convert('RGB')
    for fy in (.62, .66, .70, .74, .78):
        x, y = W // 2, int(H * fy)
        r, g, b = rgb.getpixel((x, y))
        if min(r, g, b) > 200:
            ImageDraw.floodfill(rgb, (x, y), (255, 0, 255), thresh=60)
    r, g, b = rgb.split()
    hole = ImageChops.multiply(ImageChops.multiply(r.point(lambda v: 255 if v == 255 else 0), b.point(lambda v: 255 if v == 255 else 0)), g.point(lambda v: 255 if v == 0 else 0))
    hole = hole.filter(ImageFilter.MaxFilter(3))
    a = ImageChops.subtract(p.getchannel('A'), hole)
    p.putalpha(a); return p
hats = [clear_hole(h) for h in hats]
scarves = grid(sheet('scarf2'), 1, 5)
vest6 = grid(sheet('vest2'), 2, 3)        # none, one, jacket / two, two, three
vests = dict(zip(['none', 'one', 'jacket', 'two', '_', 'three'], vest6))
ears = grid(sheet('ears2'), 1, 4)         # plain, torn, plaster, earring
teeth = grid(sheet('teeth'), 1, 5)        # (first set) silver, gap, gold, two gold, the scar: only the scar used
mouths = grid(sheet('mouth'), 1, 5)       # plain, silver, gap, gold, two gold

# where things go on the base (its pixels: head 195..1605 wide, top 555; muzzle top 1005; mouth 900,1440; ears at
# 390,645 and 1410,645)
L = dict(eyes=(900, 985), eyes_w=900, mouth=(900, 1445), mouth_w=330, mouth_squash=.7, ear_r=(1412, 640), ear_w=360,
         hat=(900, 565), hat_w=860, scarf=(930, 1870), scarf_w=960, vest=(900, 2100), vest_w=1560, vest_squash=.56, scar_h=175)
SCARS = dict(below=(1300, 1110, 20), nose=(900, 1110, 90), cheek=(470, 1200, -20), above=(560, 830, 15), mouth=(1110, 1500, 10))

parts = {}
ke = L['eyes_w'] / eyes['small-thick'].width   # one scale for all eyes, as on the sheet
for oid in ['big-thin', 'sleepy-thick', 'big-thick', 'small-thin', 'small-thick']:
    lay = layer(); p = eyes[oid]; place(lay, p, *L['eyes'], p.width * ke); parts['eyes-' + oid] = lay
# the mouth: the base's closed smile painted over with the muzzle's colour (soft edges), the open grin on it
def muzzle_patch(lay):
    patch = Image.new('RGBA', (BW, BH), (225, 179, 137, 0))
    m = Image.new('L', (BW, BH), 0); ImageDraw.Draw(m).ellipse((690, 1355, 1110, 1505), fill=255)
    patch.putalpha(m.filter(ImageFilter.GaussianBlur(10))); lay.alpha_composite(patch)
km = L['mouth_w'] / mouths[0].width
for oid, p in zip(['plain', 'silver', 'gap', 'gold', 'two-gold'], mouths):
    lay = layer(); muzzle_patch(lay); place(lay, p, *L['mouth'], p.width * km, squash=L['mouth_squash']); parts['teeth-' + oid] = lay
# the scar: a deep red-brown (its own colours were close to the fur), its shading kept
scar = teeth[4].copy(); r, g, b, a = scar.split()
lum = Image.merge('RGB', (r, g, b)).convert('L')
scar = Image.merge('RGBA', (lum.point(lambda v: 60 + v * 70 // 255), lum.point(lambda v: 14 + v * 30 // 255), lum.point(lambda v: 12 + v * 25 // 255), a.point(lambda v: min(255, v * 2))))
for oid, (x, y, a) in SCARS.items():
    lay = layer(); place(lay, scar, x, y, L['scar_h'] * scar.width / scar.height, rot=a); parts['scar-' + oid] = lay
kh = L['hat_w'] / hats[4].width
for oid, p in zip(['red-yellow', 'green-white', 'blue-yellow', 'green-plain', 'green-yellow'], hats):
    lay = layer(); place(lay, p, *L['hat'], p.width * kh); parts['hat-' + oid] = lay
# ears: the base has plain ears; an option is laid over the right one (both: a plaster on the left one too)
plain, torn, plaster, ring = ears
kr = L['ear_w'] / plain.width
def ear(lay, p, right=True):
    x, y = L['ear_r']
    place(lay, p, x if right else BW - x, y + (p.height - plain.height) * kr / 2, p.width * kr, flip=not right)
parts['ears-plain'] = layer()
for oid, p in (('torn', torn), ('one', plaster), ('earring', ring)):
    lay = layer(); ear(lay, p); parts['ears-' + oid] = lay
lay = layer(); ear(lay, plaster); ear(lay, plaster, right=False); parts['ears-both'] = lay
ks = L['scarf_w'] / scarves[4].width
for oid, p in zip(['blue-dots', 'red-stripes', 'red-plain', 'green-dots', 'red-dots'], scarves):
    lay = layer(); place(lay, p, *L['scarf'], p.width * ks); parts['scarf-' + oid] = lay
kv = L['vest_w'] / vests['two'].width
for oid in ['none', 'one', 'jacket', 'two', 'three']:
    p = vests[oid]; lay = layer(); place(lay, p, *L['vest'], p.width * kv, squash=L['vest_squash']); parts['vest-' + oid] = lay

ORDER = ['base', 'vest', 'scarf', 'ears', 'head', 'eyes', 'teeth', 'hat', 'scar']
if 'preview' in sys.argv:
    out = sys.argv[sys.argv.index('preview') + 1]
    looks = [dict(vest='two', scarf='red-dots', ears='one', eyes='small-thick', teeth='gold', hat='green-yellow', scar='above'),
             dict(vest='jacket', scarf='blue-dots', ears='earring', eyes='big-thin', teeth='gap', hat='red-yellow', scar='cheek'),
             dict(vest='three', scarf='red-stripes', ears='torn', eyes='sleepy-thick', teeth='two-gold', hat='blue-yellow', scar='mouth'),
             dict(vest='one', scarf='green-dots', ears='both', eyes='big-thick', teeth='silver', hat='green-white', scar='below'),
             dict(vest='none', scarf='red-plain', ears='plain', eyes='small-thin', teeth='plain', hat='green-plain', scar='nose')]
    row = Image.new('RGB', (5 * 320, 400), 'white')
    for i, look in enumerate(looks):
        c = base.copy()
        for n in ORDER[1:]: c.alpha_composite(head if n == 'head' else parts[f'{n}-{look[n]}'])
        row.paste(c.crop(FRAME).convert('RGB').resize((320, 400)), (i * 320, 0))
    row.save(out)
    sys.exit()
save(base, 'base'); save(head, 'head')
for name, img in parts.items(): save(img, name)
print('saved', len(parts) + 2, 'layers')

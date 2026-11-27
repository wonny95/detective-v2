"""Recipe box case (design/case-recipe-box.md, "그림·녹음"): the kitchen in the back of Suzy's chocolate shop as the place.

One tall 3:4 picture (Higgsfield Nano Banana 2.1 2K, 1792×2400) scaled to 1376 wide, cut as the Valentine shop
(scripts/cut-valentine-places.py): a 1376×1056 band from TOP is the place (the wall shelf with the cookbooks, the
stove and the worktable with the tiles in front of it), the rest under it the floor (kitchen-floor.jpg, mirrored on to
FLOOR_H, as the other places).
- kitchen-higgsfield-original.png  job 9b399ebd-11d0-4283-93b8-98e4a6ce2787 (reference: shop v2 job b2aecb5f, user
  2026-11-27: the kitchen instead of the shop). The worktable top and the gap on the shelf are left empty for the box,
  the note and the recipe book, which code puts on them.
- kitchen-props-higgsfield-original.png  job d851a157-e7e7-45e6-bae6-c74edf2fa993 (references: the kitchen job and the prop
  sheet job d033c844; user 2026-11-27: the props cut from the sheet did not match the room's angle, so the same kitchen
  was drawn again with the closed recipe box and the folded note on the worktable and the recipe book on the shelf)
  -> scene-box.webp, scene-note.webp, scene-book.webp: only where the two pictures differ inside each object's box (the
  two differ a little everywhere in their strokes, so each patch has a soft edge), placed by code when it is unlocked.
Run from the project folder: python -I scripts/cut-recipe-places.py   (Pillow only)"""
from PIL import Image, ImageChops, ImageDraw, ImageFilter

P = 'assets/places/recipe/'
H, FLOOR_H = 1056, 900
PLACES = {'kitchen': ('kitchen-higgsfield-original.png', 230)}

for name, (src, top) in PLACES.items():
    im = Image.open(P + src).convert('RGB')
    im = im.resize((1376, round(im.height * 1376 / im.width)), Image.LANCZOS)
    im.crop((0, top, 1376, top + H)).save(P + name + '.webp', quality=88)
    rest = im.crop((0, top + H, 1376, im.height))
    floor = Image.new('RGB', (1376, FLOOR_H)); y, flip = 0, False
    while y < FLOOR_H:
        floor.paste(rest.transpose(Image.FLIP_TOP_BOTTOM) if flip else rest, (0, y)); y += rest.height; flip = not flip
    floor.save(P + name + '-floor.jpg', quality=85)
    print(name, im.size, 'band', top, '-', top + H, 'floor from', rest.height)

# the props drawn into the kitchen: the props picture over the plain one, cut where the two differ, soft-edged
TOP, k = PLACES['kitchen'][1], 1376 / 1792
PATCHES = {   # in the 1792 originals
    'scene-box':  (1315, 995, 1575, 1215),
    'scene-note': (1425, 1175, 1610, 1290),
    'scene-book': (625, 340, 805, 660),
}
a = Image.open(P + 'kitchen-higgsfield-original.png').convert('RGB')
b = Image.open(P + 'kitchen-props-higgsfield-original.png').convert('RGB')
a, b = (im.resize((1376, round(im.height * k)), Image.LANCZOS) for im in (a, b))
for name, box in PATCHES.items():
    x0, y0, x1, y1 = (round(v * k) for v in box)
    # the cream box and note are close in colour to the wall and the light wood, so a low threshold; the objects are
    # convex, so the mask is the convex hull of the changed pixels (the inside of the note barely changes at all)
    d = ImageChops.difference(a.crop((x0, y0, x1, y1)), b.crop((x0, y0, x1, y1))).convert('L').point(lambda v: 255 if v > 30 else 0)
    d = d.filter(ImageFilter.MinFilter(3))
    pts = sorted((x, y) for y in range(0, d.height, 2) for x in range(0, d.width, 2) if d.getpixel((x, y)))
    cross = lambda o, p, q: (p[0] - o[0]) * (q[1] - o[1]) - (p[1] - o[1]) * (q[0] - o[0])
    hull = []
    for seq in (pts, pts[::-1]):
        part = []
        for q in seq:
            while len(part) >= 2 and cross(part[-2], part[-1], q) <= 0: part.pop()
            part.append(q)
        hull += part[:-1]
    d = Image.new('L', d.size); ImageDraw.Draw(d).polygon(hull, fill=255)
    d = d.filter(ImageFilter.MaxFilter(5))
    edge = Image.new('L', d.size); ImageDraw.Draw(edge).rectangle((5, 5, d.width - 6, d.height - 6), fill=255)
    mask = ImageChops.multiply(d, edge).filter(ImageFilter.GaussianBlur(4))
    patch = b.crop((x0, y0, x1, y1)).convert('RGBA'); patch.putalpha(mask)
    patch.save(P + name + '.webp', quality=90, method=6)
    print(name, patch.size, 'at', x0, y0 - TOP, 'in the band')

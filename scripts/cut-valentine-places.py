"""Valentine case (design/case-valentine-chocolate.md, "그림 제작 계획" 1·2): the classroom and the chocolate shop as places.

Each is one tall 3:4 picture (Higgsfield Nano Banana 2.1 2K, 1792×2400) scaled to 1376 wide. A 1376×1056 band from TOP
is the place (taller than 768, as the twins case's places: the classroom's chalkboard and the desk with the floor in
front of it, the shop's acorn sign and the counter with the tiles beside it, all in one band), the rest under it the
floor (<place>-floor.jpg, mirrored on to FLOOR_H, as the other places).
- classroom-v2-higgsfield-original.png  job b08df850-2c2f-4080-97db-560a2c3e4458 (user 2026-11-27: v1 job 85836301 looked
  bare and not like a school; v2 has books, a notice board, a clock and pupils' desks, one chalk heart)
- classroom-v2-boxes-higgsfield-original.png  job 2db2b8d7-181c-4cde-8c54-560c30247efc: the same with the chocolate box and
  small gift boxes on the teacher's desk -> desk-boxes.webp, only the desk part (the two pictures differ a little
  everywhere in their strokes, so the patch has a soft edge and keeps to where the boxes are)
- shop-v2-higgsfield-original.png    job b2aecb5f-dc48-4b87-99eb-4385a56d46b0
Run from the project folder: python -I scripts/cut-valentine-places.py   (Pillow only)"""
from PIL import Image, ImageChops, ImageDraw, ImageFilter

P = 'assets/places/valentine/'
H, FLOOR_H = 1056, 900
PLACES = {'classroom': ('classroom-v2-higgsfield-original.png', 300), 'shop': ('shop-v2-higgsfield-original.png', 230)}

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

# the boxes on the teacher's desk: the boxed picture over the plain one, cut where the two differ (desk top), soft-edged
BOX = (590, 1040, 1200, 1290)   # in the 1792 originals: the big box and the stack of small boxes on the desk
k = 1376 / 1792
a = Image.open(P + 'classroom-v2-higgsfield-original.png').convert('RGB')
b = Image.open(P + 'classroom-v2-boxes-higgsfield-original.png').convert('RGB')
a, b = (im.resize((1376, round(im.height * k)), Image.LANCZOS) for im in (a, b))
x0, y0, x1, y1 = (round(v * k) for v in BOX)
d = ImageChops.difference(a.crop((x0, y0, x1, y1)), b.crop((x0, y0, x1, y1))).convert('L').point(lambda v: 255 if v > 45 else 0)
d = d.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(15))
edge = Image.new('L', d.size); ImageDraw.Draw(edge).rectangle((6, 6, d.width - 7, d.height - 7), fill=255)
mask = ImageChops.multiply(d, edge).filter(ImageFilter.GaussianBlur(4))
patch = b.crop((x0, y0, x1, y1)).convert('RGBA'); patch.putalpha(mask)
patch.save(P + 'desk-boxes.webp', quality=90, method=6)
print('desk-boxes.webp', patch.size, 'at', x0, y0 - PLACES['classroom'][1], 'in the band')
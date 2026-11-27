"""Valentine case (design/case-valentine-chocolate.md, "그림 제작 계획" 1·2): the classroom and the chocolate shop as places.

Each is one tall 3:4 picture (Higgsfield Nano Banana 2.1 2K, 1792×2400) scaled to 1376 wide. A 1376×1056 band from TOP
is the place (taller than 768, as the twins case's places: the classroom's chalkboard and the desk with the floor in
front of it, the shop's acorn sign and the counter with the tiles beside it, all in one band), the rest under it the
floor (<place>-floor.jpg, mirrored on to FLOOR_H, as the other places).
- classroom-higgsfield-original.png  job 85836301-1089-4373-8718-5dce4b8d54d9
- shop-v2-higgsfield-original.png    job b2aecb5f-dc48-4b87-99eb-4385a56d46b0
Run from the project folder: python -I scripts/cut-valentine-places.py   (Pillow only)"""
from PIL import Image

P = 'assets/places/valentine/'
H, FLOOR_H = 1056, 900
PLACES = {'classroom': ('classroom-higgsfield-original.png', 300), 'shop': ('shop-v2-higgsfield-original.png', 230)}

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

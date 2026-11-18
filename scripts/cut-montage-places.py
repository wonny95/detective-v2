"""The robbery case's pictures (Case 03, design/case-03-bear-town-montage.md), from the Higgsfield originals in
assets/places/montage/:
- shop-v2-higgsfield-original.png (job a9d09de1, the street by the honey shop, one tall 3:4 picture as the kite park;
  user rule 2026-11-18: place pictures tall, not wide) scaled to 1376 wide: a 1376x768 band from TOP is the place
  (shop.webp), the street under it its floor (shop-floor.jpg, ART_FLOOR), mirrored on to FLOOR_H. The first, wide try
  (shop-higgsfield-original.png, job 8f600778) is kept on disk, not cut.
- wanted-higgsfield-original.png (job 709ef60d, the wanted poster on a cork board) -> wanted.jpg, the poster alone
  (the children's drawings round it left out): the case card's cover and the review photo
Run from the project folder: python -I scripts/cut-montage-places.py"""
from PIL import Image
D = 'assets/places/montage/'
TOP, FLOOR_H = 640, 900
im = Image.open(D + 'shop-v2-higgsfield-original.png').convert('RGB')
im = im.resize((1376, round(im.height * 1376 / im.width)), Image.LANCZOS)
im.crop((0, TOP, 1376, TOP + 768)).save(D + 'shop.webp', quality=88)
street = im.crop((0, TOP + 768, 1376, im.height))
floor = Image.new('RGB', (1376, FLOOR_H)); y, flip = 0, False
while y < FLOOR_H:
    floor.paste(street.transpose(Image.FLIP_TOP_BOTTOM) if flip else street, (0, y)); y += street.height; flip = not flip
floor.save(D + 'shop-floor.jpg', quality=85)
w = Image.open(D + 'wanted-higgsfield-original.png').convert('RGB')
k = w.width / 1200   # the box was read on a 1200 px wide copy
w.crop(tuple(round(v * k) for v in (240, 30, 960, 870))).resize((864, 1008), Image.LANCZOS).save(D + 'wanted.jpg', quality=88)
print('shop', im.size, 'street h', street.height, 'floor', floor.size)

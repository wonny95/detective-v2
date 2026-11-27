"""Recipe box case (design/case-recipe-box.md, "레시피북의 쪽"): cut the 15 recipe-book foods and the lemon cake out of the
magenta food sheet.

- food-sheet-higgsfield-original.png  job db7eaaf0-5a03-48fa-8f0e-3780b4d89a94 (Nano Banana 2.1 16:9 2K, references: the
  prop sheet job d033c844 and the kitchen job 9b399ebd for the style). Asked for a 4×4 grid, it drew 5 columns with a
  second muffin, a plain layered cake and a second apple pie (not used) and the lollipops across rows 3 and 4.
Output: assets/places/recipe/food/<name>.webp, trimmed to the picture (each on its plate with a white sticker edge).
Run from the project folder: python -I scripts/cut-recipe-food.py   (Pillow only)"""
import os
from PIL import Image, ImageFilter

P = 'assets/places/recipe/'
OUT = P + 'food/'
os.makedirs(OUT, exist_ok=True)
im = Image.open(P + 'food-sheet-higgsfield-original.png').convert('RGB')
W, H = im.size
px = im.load()

alpha = Image.new('L', (W, H))
ap = alpha.load()
for y in range(H):
    for x in range(W):
        r, g, b = px[x, y]
        ap[x, y] = 0 if (r > 150 and b > 150 and g < 120 and abs(r - b) < 90) else 255
alpha = alpha.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1))
rgba = im.convert('RGBA'); rgba.putalpha(alpha)

S = W / 1400   # boxes below were read on a 1400-wide view of the sheet
BOXES = {
    'rice-cake':     (35, 55, 310, 215),
    'jam-roll':      (325, 35, 585, 215),
    'scones':        (595, 35, 860, 220),
    'muffins':       (875, 40, 1115, 215),
    'nut-cookies':   (35, 235, 315, 400),
    'gingerbread':   (355, 235, 540, 445),
    'egg-tart':      (575, 245, 840, 410),
    'honey-cake':    (860, 245, 1120, 410),
    'oatmeal-bread': (40, 425, 300, 590),
    'lollipops':     (335, 475, 560, 740),
    'cookies':       (585, 430, 835, 580),
    'apple-pie':     (865, 430, 1120, 590),
    'toffee':        (35, 600, 305, 745),
    'pancakes':      (580, 595, 830, 750),
    'brownies':      (860, 600, 1110, 750),
    'lemon-cake':    (1130, 590, 1375, 750),
}
for name, box in BOXES.items():
    x0, y0, x1, y1 = (round(v * S) for v in box)
    part = rgba.crop((x0, y0, x1, y1))
    part = part.crop(part.getchannel('A').point(lambda v: 255 if v > 40 else 0).getbbox())
    part.save(OUT + name + '.webp', quality=90, method=6)
    print(name, part.size)

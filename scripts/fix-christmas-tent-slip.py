"""Coco's hand-over slip (user request: a clue that shows whether Coco or Nico tells the truth about the boxes):
Higgsfield drew a blank sheet beside Coco's snowflake table (assets/places/christmas/tent-slip-higgsfield-original.png);
only that sheet is pasted over tent.jpg with soft edges. The words are drawn by the game (cocoSlip() in index.html).
Run from the project folder with the old tent.jpg as the argument: python scripts/fix-christmas-tent-slip.py <old.jpg>"""
import sys
from PIL import Image, ImageDraw, ImageFilter, ImageChops
old = Image.open(sys.argv[1]).convert('RGB')
fix = Image.open('assets/places/christmas/tent-slip-higgsfield-original.png').convert('RGB').resize(old.size, Image.LANCZOS)
d = ImageChops.difference(old, fix).convert('L').crop((600, 100, 1376, 768))
print('mean diff outside the sheet', sum(d.crop((0, 0, 300, 300)).getdata()) / 90000)
mask = Image.new('L', old.size, 0)
ImageDraw.Draw(mask).rectangle((1022, 515, 1222, 692), 255)
old.paste(fix, (0, 0), mask.filter(ImageFilter.GaussianBlur(6)))
old.save('assets/places/christmas/tent.jpg', quality=92)

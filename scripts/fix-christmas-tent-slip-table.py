"""Coco's slip off the floor (user request: on the floor it looked odd; user pick: onto her snowflake table). The sheet
Higgsfield drew on the floor (scripts/fix-christmas-tent-slip.py) is covered again with the floor of the picture from
before it (git e096264), soft-edged; the slip itself is now drawn by the game on the table (cocoSlip() in index.html).
Run from the project folder with that older tent.jpg as the argument: python scripts/fix-christmas-tent-slip-table.py <old.jpg>"""
import sys
from PIL import Image, ImageDraw, ImageFilter
old = Image.open(sys.argv[1]).convert('RGB')
cur = Image.open('assets/places/christmas/tent.jpg').convert('RGB')
mask = Image.new('L', cur.size, 0)
ImageDraw.Draw(mask).rectangle((1016, 509, 1228, 698), 255)
cur.paste(old, (0, 0), mask.filter(ImageFilter.GaussianBlur(6)))
cur.save('assets/places/christmas/tent.jpg', quality=92)

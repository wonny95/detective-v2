"""Kite case (Case 01, 2026-11-18): the park, one tall Higgsfield picture (park-higgsfield-original.png, job bcf37434) cut
as the umbrella hall: scaled to 1376 wide, a 1376x768 band from TOP is the place (park.webp), the rest its floor
(park-floor.jpg, ART_FLOOR). The five kites (kites-sheet-original.png, job 8b6a428e) are cut to kite-1..5.png (white
paper made transparent) and laid over the trees by ART.park. Run from the project folder: python -I scripts/cut-kite-places.py"""
from PIL import Image
D = 'assets/places/kite/'
TOP = 330
im = Image.open(D + 'park-higgsfield-original.png').convert('RGB')
im = im.resize((1376, round(im.height * 1376 / im.width)), Image.LANCZOS)
im.crop((0, TOP, 1376, TOP + 768)).save(D + 'park.webp', quality=88)
floor = im.crop((0, TOP + 768, 1376, im.height)); floor.save(D + 'park-floor.jpg', quality=85)
print('park', im.size, 'floor h', floor.height)

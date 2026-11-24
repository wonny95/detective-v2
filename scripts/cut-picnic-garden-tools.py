# The garden with Mia's bag open on the bench (user decision 2026-11-24): a Higgsfield edit (Nano Banana Pro, job
# d8938af8) of the garden's 3:4 outpaint (garden-outpaint-original.jpg) with the blue bag (bag-blue-higgsfield-original)
# and the red one (backpack-red) as references -> garden-tools-higgsfield-original.png.
# Cut the same way as the old garden: the band the place view shows is where the old picture (garden.webp) sits in
# the old outpaint, the talk floor (ART_FLOOR) everything under it. Both come out of the one new picture, so there is
# no seam. The old pictures are kept as garden-plain.webp and garden-floor-plain.jpg.
# Run from the repo root: python -X utf8 -I scripts/cut-picnic-garden-tools.py   (Pillow only)
import os
from PIL import Image, ImageChops, ImageStat

D = 'assets/places/picnic-storyboard/'
if not os.path.exists(D + 'garden-plain.webp'):
    os.replace(D + 'garden.webp', D + 'garden-plain.webp')
    os.replace(D + 'garden-floor.jpg', D + 'garden-floor-plain.jpg')
art = Image.open(D + 'garden-plain.webp').convert('RGB')
old = Image.open(D + 'garden-outpaint-original.jpg').convert('RGB')
new = Image.open(D + 'garden-tools-higgsfield-original.png').convert('RGB').resize(old.size, Image.LANCZOS)
w, h = art.size
scale = old.width / w
SMALL = 256
k = SMALL / old.width
a = art.resize((SMALL, round(h * scale * k)), Image.LANCZOS)
o = old.resize((SMALL, round(old.height * k)), Image.LANCZOS)
diff = lambda y: sum(ImageStat.Stat(ImageChops.difference(o.crop((0, y, SMALL, y + a.height)), a)).mean)
y = min(range(o.height - a.height + 1), key=diff)
top, bottom = round(y / k), round((y + a.height) / k)
new.crop((0, top, new.width, bottom)).resize((w, h), Image.LANCZOS).save(D + 'garden.webp', quality=90)
floor = new.crop((0, bottom, new.width, new.height))
floor.resize((w, round(floor.height / scale)), Image.LANCZOS).save(D + 'garden-floor.jpg', quality=90)
print('band', top, '-', bottom, 'of', new.height, '(match', round(diff(y), 1), ')')

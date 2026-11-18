"""Kite case (Case 01, 2026-11-18): the park, one tall Higgsfield picture cut as the umbrella hall: scaled to 1376 wide,
a 1376x768 band from TOP is the place (park.webp), the rest its floor (park-floor.jpg, ART_FLOOR).
The park is the redrawn one (park-v3-higgsfield-original.png, job 901961d9, user request: the people stood up among
the fence and bushes): its ground line is still low, so the band starts further down (TOP 640: the lower tree crowns,
the fence, the path and lawn at the bottom, where the people stand). The lawn left under the band is short, so the
floor goes on with it mirrored. The first park (park-higgsfield-original.png, job bcf37434) and the try that came out
like it (park-v2-higgsfield-original.png) are kept on disk, not cut.
The flower bed's painted flowers are taken out (user request 2026-11-18: they looked odd with the drawn bunches that
part over a kite): the bed redrawn without them by Higgsfield from a crop of the band (bed-noflowers-original.png, job
7a46a0f3, the crop at BED_CROP of the full-size band), its colours matched to the band's, and only the bed (BED_MASK,
soft edge) pasted back, in the full-size band and in park.webp; the bunches are drawn over it (kitesArt, bedSlot).
The kites are drawn over it by ART.park (KITE_SLOTS; scripts/cut-kites-v2.py, scripts/make-kite-leaves.py).
Run from the project folder: python -I scripts/cut-kite-places.py"""
from PIL import Image, ImageDraw, ImageFilter, ImageStat
D = 'assets/places/kite/'
TOP, FLOOR_H = 640, 900
im = Image.open(D + 'park-v3-higgsfield-original.png').convert('RGB')
im = im.resize((1376, round(im.height * 1376 / im.width)), Image.LANCZOS)
# the same band at the original's full size (1792 wide), drawn in the park and its close looks (KITE_ZOOM)
full = Image.open(D + 'park-v3-higgsfield-original.png').convert('RGB'); f = full.width / 1376
band = full.crop((0, round(TOP * f), full.width, round((TOP + 768) * f)))
# the flower bed without its flowers: crop box in the full-size band, the bed in that crop
BED_CROP, BED_MASK = (480, 470, 1320, 830), (104, 132, 752, 262)
src = band.crop(BED_CROP); bed = Image.open(D + 'bed-noflowers-original.png').convert('RGB').resize(src.size, Image.LANCZOS)
ref = (104, 262, 752, 300)   # the planter frame, the same in both: match the redraw's colours to the band's
a, b = ImageStat.Stat(src.crop(ref)), ImageStat.Stat(bed.crop(ref))
bed = Image.merge('RGB', [ch.point(lambda v, i=i: max(0, min(255, round((v - b.mean[i]) * a.stddev[i] / max(b.stddev[i], 1) + a.mean[i])))) for i, ch in enumerate(bed.split())])
m = Image.new('L', src.size, 0); ImageDraw.Draw(m).rectangle(BED_MASK, fill=255); m = m.filter(ImageFilter.GaussianBlur(6))
band.paste(bed, BED_CROP[:2], m)
band.save(D + 'park-hi.webp', quality=90)
im.paste(band.resize((1376, 768), Image.LANCZOS), (0, TOP))
im.crop((0, TOP, 1376, TOP + 768)).save(D + 'park.webp', quality=88)
lawn = im.crop((0, TOP + 768, 1376, im.height))
floor = Image.new('RGB', (1376, FLOOR_H))
y, flip = 0, False
while y < FLOOR_H:
    floor.paste(lawn.transpose(Image.FLIP_TOP_BOTTOM) if flip else lawn, (0, y)); y += lawn.height; flip = not flip
floor.save(D + 'park-floor.jpg', quality=85)
print('park', im.size, 'lawn h', lawn.height, 'floor h', FLOOR_H)

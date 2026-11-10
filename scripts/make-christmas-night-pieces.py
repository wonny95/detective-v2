# The square's floor under the picture (tree-floor.jpg) for the night: each colour channel is mapped so the day
# picture's bottom strip matches the night picture's (mean and spread), the way tree-night.jpg was darkened from the
# day picture. The lit square's floor and sky come straight from its Higgsfield picture (the lit sky / floor block).
# Run from the project folder: python scripts/make-christmas-night-pieces.py
from PIL import Image, ImageStat
D = 'assets/places/christmas/'
day = Image.open(D + 'tree.jpg').convert('RGB')
floor = Image.open(D + 'tree-floor.jpg').convert('RGB')
strip = lambda im: ImageStat.Stat(im.crop((0, im.height - 120, im.width, im.height)))
for name in ('night',):
    s, t = strip(day), strip(Image.open(D + f'tree-{name}.jpg').convert('RGB'))
    bands = [band.point(lambda v, c=c: max(0, min(255, round((v - s.mean[c]) * t.stddev[c] / s.stddev[c] + t.mean[c]))))
             for c, band in enumerate(floor.split())]
    out = Image.merge('RGB', bands)
    out.save(D + f'tree-floor-{name}.jpg', quality=88)
    print(name, [round(v) for v in ImageStat.Stat(out).mean])

# the lit picture as scale-and-band cut it (scripts/cut-christmas-assets.py, top 330): above the band its sky with the
# tree's top and gold star, below it its floor
lit = Image.open(D + 'tree-lit-higgsfield-original.jpg').convert('RGB').resize((1376, 1843), Image.LANCZOS)
lit.crop((0, 0, 1376, 330)).save(D + 'tree-lit-sky.jpg', quality=88)
lit.crop((0, 1098, 1376, 1843)).save(D + 'tree-floor-lit.jpg', quality=85)

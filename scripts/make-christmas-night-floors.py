# The square's floor under the picture (tree-floor.jpg) for the night and the lit tree: each colour channel is mapped
# so the day picture's bottom strip matches the night / lit picture's (mean and spread), the way tree-night.jpg was
# darkened from the day picture. Run from the project folder: python scripts/make-christmas-night-floors.py
from PIL import Image, ImageStat
D = 'assets/places/christmas/'
day = Image.open(D + 'tree.jpg').convert('RGB')
floor = Image.open(D + 'tree-floor.jpg').convert('RGB')
strip = lambda im: ImageStat.Stat(im.crop((0, im.height - 120, im.width, im.height)))
for name in ('night', 'lit'):
    s, t = strip(day), strip(Image.open(D + f'tree-{name}.jpg').convert('RGB'))
    bands = [band.point(lambda v, c=c: max(0, min(255, round((v - s.mean[c]) * t.stddev[c] / s.stddev[c] + t.mean[c]))))
             for c, band in enumerate(floor.split())]
    out = Image.merge('RGB', bands)
    out.save(D + f'tree-floor-{name}.jpg', quality=88)
    print(name, [round(v) for v in ImageStat.Stat(out).mean])

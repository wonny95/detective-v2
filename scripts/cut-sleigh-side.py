"""The sleigh place drawn again beside the tent, the storeroom far off with the runner marks from its back door to
the sleigh (user request: the old spot in front of the tent was too open for sneaking off, and the marks could not be
followed). Cuts sleigh-side-higgsfield-original.jpg at 1376x1843: the place is the top 1028 (taller than the other places so
the storeroom far off shows, user pick; artHeight 1028 in index.html), the rest its floor and draws the marks lighter (user: too dark).
usage: python scripts/cut-sleigh-side.py
"""
from PIL import Image, ImageDraw, ImageFilter

PL = 'assets/places/christmas/'
im = Image.open(f'{PL}sleigh-side-higgsfield-original.jpg').convert('RGB').resize((1376, 1843), Image.LANCZOS)
# the marks: the snow from the storeroom down past the post to the rear runner; wood, box and sack (warm) are kept
mask = Image.new('L', im.size, 0)
ImageDraw.Draw(mask).polygon([(0, 180), (330, 180), (420, 330), (700, 700), (560, 760), (330, 760), (0, 760)], fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(8))
px, m, snow = im.load(), mask.load(), (241, 244, 253)
for y in range(150, 800):
    for x in range(720):
        k = m[x, y]
        if not k: continue
        r, g, b = px[x, y]
        if b < g or r > g + 6: continue
        if sum(s - c for s, c in zip(snow, (r, g, b))) / 3 < 12: continue
        f = 1 - .5 * k / 255
        px[x, y] = tuple(min(255, int(s - (s - c) * f)) for s, c in zip(snow, (r, g, b)))
im.crop((0, 0, 1376, 1028)).save(f'{PL}sleigh.jpg', quality=88)
im.crop((0, 1028, 1376, 1843)).save(f'{PL}sleigh-floor.jpg', quality=85)
print('ok')

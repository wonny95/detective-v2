"""Tess's working pose for the Christmas tent (user request: her body turned to the gift table): the Higgsfield picture
on white (assets/characters/tess-work-higgsfield-original.png) cut out by flooding the white in from the edges,
trimmed and scaled to 700 px high -> assets/characters/tess-work.png. Pillow only.
usage: python scripts/cut-tess-work.py"""
from PIL import Image, ImageDraw, ImageFilter
src = Image.open('assets/characters/tess-work-higgsfield-original.png').convert('RGB')
W, H = src.size
# flood the near-white background from every edge pixel into a marker colour
work = src.copy()
for x, y in [(x, 0) for x in range(0, W, 8)] + [(x, H - 1) for x in range(0, W, 8)] + [(0, y) for y in range(0, H, 8)] + [(W - 1, y) for y in range(0, H, 8)]:
    if work.getpixel((x, y)) != (255, 0, 255) and min(work.getpixel((x, y))) > 225:
        ImageDraw.floodfill(work, (x, y), (255, 0, 255), thresh=40)
mask = Image.eval(work, lambda v: v).convert('RGB')
bg = Image.new('L', (W, H), 0)
px, mp = work.load(), bg.load()
for y in range(H):
    for x in range(W):
        if px[x, y] == (255, 0, 255): mp[x, y] = 255
alpha = bg.point(lambda v: 255 - v).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(.7))
out = src.convert('RGBA'); out.putalpha(alpha)
box = alpha.point(lambda v: 255 if v > 40 else 0).getbbox(); out = out.crop(box)
m = int(max(out.size) * .03); pad = Image.new('RGBA', (out.width + 2 * m, out.height + 2 * m), (0, 0, 0, 0)); pad.paste(out, (m, m))
pad = pad.resize((round(pad.width * 700 / pad.height), 700), Image.LANCZOS)
pad.save('assets/characters/tess-work.png', optimize=True)
print(pad.size)

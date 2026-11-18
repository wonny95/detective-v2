"""Kite case: the six kites of different shapes (user request 2026-11-18: not all one shape; the shape is a clue),
colourful, the tails of many kinds (user request: not a few colours, no ribbons on a bird), one Higgsfield sheet on white
(kites-v3-sheet-original.png, job 80d43285; the first, all red with ribbon tails, kites-v2-sheet-original.png, is kept):
left to right red-and-yellow bird with two long tails (Toby's), the same with one tail, the same with two short tails,
blue-and-green bird, purple-and-pink butterfly, orange fish with blue stripes -> kite2-1..6.png, the white made
transparent (soft edge), each cut to itself + 8 px. Prints each size. Run: python -I scripts/cut-kites-v2.py"""
from PIL import Image, ImageChops, ImageFilter
D = 'assets/places/kite/'
src = Image.open(D + 'kites-v3-sheet-original.png').convert('RGB')
W, H = src.size
# ink: anything clearly darker or more coloured than the white paper
g = src.convert('L'); sat = ImageChops.subtract(src.convert('HSV').getchannel('S'), Image.new('L', src.size, 0))
ink = ImageChops.lighter(g.point(lambda v: 255 if v < 232 else 0), sat.point(lambda v: 255 if v > 40 else 0))
cols = [any(ink.getpixel((x, y)) for y in range(0, H, 3)) for x in range(W)]
runs, x = [], 0
while x < W:
    if cols[x]:
        s = x
        while x < W and cols[x]: x += 1
        if x - s > 40: runs.append((s, x))
    x += 1
print('columns', runs)
alpha = ink.filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.GaussianBlur(1))
im = src.convert('RGBA'); im.putalpha(alpha)
for n, (a, b) in enumerate(runs, 1):
    part = im.crop((a, 0, b, H)); box = part.getchannel('A').point(lambda v: 255 if v > 30 else 0).getbbox()
    part = part.crop((max(box[0] - 8, 0), max(box[1] - 8, 0), min(box[2] + 8, part.width), min(box[3] + 8, H)))
    part.save(D + f'kite2-{n}.png', optimize=True); print(n, part.size)

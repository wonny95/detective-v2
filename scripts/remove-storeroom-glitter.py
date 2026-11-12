"""Paint out the gold glitter in the storeroom (user request: the glitter was taken out of the story): the specks on the
star shelf and the heap on the floor below it. A speck is a pixel much brighter than the wood around it in its row; its
dark rim is the darker pixels right beside it. The mask is filled by diffusion from the wood around it. Works on the
place pictures and on the Higgsfield original, so a re-cut stays clean. Pillow only.
usage: python scripts/remove-storeroom-glitter.py   (run it on the uncleaned pictures; a second run finds nothing)
"""
from PIL import Image, ImageFilter

PL = 'assets/places/christmas/'
# in the 1376x768 place picture: (box, how much brighter than the row's wood a speck is, which pixels are floor:
# on the floor, below the wall's baseboard, which runs down from (1077,510) at 1.11 and clear of the basket's rim at the bottom left)
# grow: how far round the specks the hole spreads (the heap sits on a brownish halo); along: the direction the hole is
# filled from, along the shelf's grain (across) or along the floor's planks, so their lines run on through it
BOXES = [((1240, 274, 1376, 324), 70, lambda x, y: True, 5, (1, 0)),
         ((975, 520, 1135, 630), 40, lambda x, y: y > 510 + (x - 1077) * 1.11 + 3 and not (x < 1012 and y > 598), 15, (.437, .9))]

def clean(path, box, thr, floor, grow, along, scale=1.0, dy=0):
    im = Image.open(path).convert('RGB')
    x0, y0, x1, y1 = [round(v * scale) for v in (box[0], box[1] + dy, box[2], box[3] + dy)]
    x1 = min(x1, im.width)
    px = im.load()
    lum = lambda x, y: sum(px[x, y])
    med = {}
    bright = Image.new('L', im.size, 0); b = bright.load()
    for y in range(y0, y1):
        for x in range(x0, x1):
            near = sorted(lum(i, y) for i in range(max(0, x - 16), min(im.width, x + 17)))
            med[x, y] = near[len(near) // 2]
            r, g, bl = px[x, y]
            if lum(x, y) > med[x, y] + thr and r > g > bl: b[x, y] = 255
    rim = bright.filter(ImageFilter.MaxFilter(round(7 * scale) | 1)).load()
    mask = Image.new('L', im.size, 0); m = mask.load()
    for (x, y), md in med.items():
        if b[x, y] or rim[x, y] and lum(x, y) < md - 18: m[x, y] = 255
    mask = mask.filter(ImageFilter.MaxFilter(round(grow * scale) | 1)); m = mask.load()
    holes = [(x, y) for y in range(y0, y1) for x in range(x0, x1) if m[x, y] and floor(x / scale, y / scale - dy)]
    # first the wood either side along the grain, blended across the hole, then smoothed a little by diffusion (each hole
    # pixel the mean of its neighbours) so no streaks are left
    hole = set(holes)
    src = im.copy().load()
    def edge(x, y, sign):
        for n in range(1, 400):
            i, j = round(x + sign * n * along[0]), round(y + sign * n * along[1])
            if not (0 <= i < im.width and 0 <= j < im.height): return None
            if (i, j) not in hole: return n, src[i, j]
    for x, y in holes:
        a, c = edge(x, y, -1), edge(x, y, 1)
        if a is None or c is None: px[x, y] = (a or c)[1]; continue
        t = a[0] / (a[0] + c[0])
        px[x, y] = tuple(round(a[1][k] * (1 - t) + c[1][k] * t) for k in range(3))
    for _ in range(8):
        for x, y in holes:
            ns = [px[i, j] for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)) if 0 <= i < im.width and 0 <= j < im.height]
            px[x, y] = tuple(sum(c[k] for c in ns) // len(ns) for k in range(3))
    im.save(path, quality=92)
    print(path, len(holes))

for box, thr, floor, grow, along in BOXES:
    for name in ('storeroom', 'storeroom-noscale'):
        clean(f'{PL}{name}.jpg', box, thr, floor, grow, along)
    # the original: 1792x2400, the place band starts at 380 of its 1376x1843 copy
    clean(f'{PL}storeroom-higgsfield-original.jpg', box, thr, floor, grow, along, 1792 / 1376, 380)

"""Kite case: the leaf pictures from Higgsfield (user requests 2026-11-18: the leaves made there; then: they must look
like the park's trees, same colours and shape). One sheet on flat magenta drawn with a piece of the park's tree crowns as
its reference (leaves-sheet-v2-original.png, job 81dca195; the first sheet, leaves-sheet-original.png, job 7105fb9f, had
veined leaves in another green): four scalloped clumps with the trees' brown outline on top (wide and low, round, three
bumps, tall oval) -> leafclump-1..4.png, eight small puffs and sprigs below -> leaf-1..8.png; magenta keyed out with
despill, each cut to itself + 6 px, then the colours matched to the tree crowns of park-hi.webp (mean and spread per
channel over the drawn pixels). The clumps hide the kites in the trees, the small bits fly when a clump is cleared.
Prints each size. Run from the project folder: python -I scripts/cut-kite-leaf-sheet.py"""
from PIL import Image, ImageStat
D = 'assets/places/kite/'
src = Image.open(D + 'leaves-sheet-v2-original.png').convert('RGB')
W, H = src.size
px = src.load(); out = Image.new('RGBA', src.size); op = out.load()
for y in range(H):
    for x in range(W):
        r, g, b = px[x, y]; mag = min(r, b) - g
        a = 255 if mag < 60 else max(0, 255 - int((mag - 60) * 255 / 70))
        if a < 255 and mag > 0:
            k = min(r, b) - (g + 25)
            if k > 0: r, b = r - k, b - k
        op[x, y] = (r, g, b, a)
# colour match: the drawn pixels' mean and spread per channel -> the tree crowns' (the top of the park band)
ref = Image.open(D + 'park-hi.webp').convert('RGB').crop((650, 0, 1250, 330))
rs = ImageStat.Stat(ref); solid = out.getchannel('A').point(lambda v: 255 if v > 200 else 0)
ss = ImageStat.Stat(out.convert('RGB'), solid)
for y in range(H):
    for x in range(W):
        r, g, b, a = op[x, y]
        if a: op[x, y] = tuple(max(0, min(255, round((c - ss.mean[i]) * rs.stddev[i] / ss.stddev[i] + rs.mean[i]))) for i, c in enumerate((r, g, b))) + (a,)
A = out.getchannel('A').point(lambda v: 255 if v > 60 else 0)
def runs(vals, minlen):
    rs, i = [], 0
    while i < len(vals):
        if vals[i]:
            s = i
            while i < len(vals) and vals[i]: i += 1
            if i - s >= minlen: rs.append((s, i))
        i += 1
    return rs
rows = runs([any(A.getpixel((x, y)) for x in range(0, W, 4)) for y in range(H)], 30)
print('rows', rows)
for (y0, y1), name in zip(rows, ['leafclump', 'leaf']):
    band = A.crop((0, y0, W, y1))
    cols = runs([any(band.getpixel((x, y)) for y in range(0, y1 - y0, 3)) for x in range(W)], 20)
    for n, (x0, x1) in enumerate(cols, 1):
        part = out.crop((x0, y0, x1, y1)); bb = part.getchannel('A').point(lambda v: 255 if v > 60 else 0).getbbox()
        part = part.crop((max(bb[0] - 6, 0), max(bb[1] - 6, 0), min(bb[2] + 6, part.width), min(bb[3] + 6, part.height)))
        part.save(D + f'{name}-{n}.png', optimize=True); print(f'{name}-{n}', part.size)

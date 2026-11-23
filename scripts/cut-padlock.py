"""The spelling game's padlock (user request 2026-11-23: design option 2, a brass combination lock whose letter wheels
are dragged; locked and unlocked drawn on one sheet). Nano Banana 2.1 16:9 2K, job 3854cbc4-5032-454f-a115-443750f9d371,
the safe icon as style reference, flat magenta -> assets/ui/padlock-higgsfield-original.png (left locked, right open).
Magenta keyed out (as scripts/cut-pablo.py); both halves cropped by the same box (the union of what is drawn in each,
in each half's own coordinates) so the body and its window sit at the same place in both, then 600 px wide
-> assets/ui/padlock-closed.webp / padlock-open.webp. Prints the window (the empty dark slot) as shares of the picture,
for the wheels laid over it (.sg-wheels in index.html).
Run from the project folder: python -I scripts/cut-padlock.py"""
from PIL import Image, ImageFilter
src = Image.open('assets/ui/padlock-higgsfield-original.png').convert('RGB')
HALVES = [('closed', 125, 1250), ('open', 1478, 2604)]
def key_out(img):
    px = img.load(); W0, H0 = img.size
    rgba = img.convert('RGBA'); rp = rgba.load(); alpha = Image.new('L', img.size); ap = alpha.load()
    for y in range(H0):
        for x in range(W0):
            r, g, b = px[x, y]; k = max(0, min(r, b) - g)
            a = 255 if k < 60 else 0 if k > 150 else round(255 * (150 - k) / 90)
            ap[x, y] = a
            if 0 < a < 255 or (a == 255 and k > 25):
                rp[x, y] = (min(r, g + 40) if r > g + 40 else r, g, min(b, g + 40) if b > g + 40 else b, 255)
    rgba.putalpha(alpha.filter(ImageFilter.GaussianBlur(.6)))
    return rgba
W = max(x1 - x0 for _, x0, x1 in HALVES)
parts = {n: key_out(src.crop((x0, 0, x0 + W, src.height))) for n, x0, _ in HALVES}
boxes = [p.getchannel('A').point(lambda a: 255 if a > 24 else 0).getbbox() for p in parts.values()]
box = (min(b[0] for b in boxes), min(b[1] for b in boxes), max(b[2] for b in boxes), max(b[3] for b in boxes))
m = 12; box = (box[0] - m, box[1] - m, box[2] + m, box[3] + m)
for n, p in parts.items():
    im = p.crop(box); s = 600 / im.width
    im = im.resize((600, round(im.height * s)), Image.LANCZOS)
    im.save(f'assets/ui/padlock-{n}.webp', quality=90)
    print(n, im.size)
# the window: the dark pixels in the middle band of the locked picture
im = Image.open('assets/ui/padlock-closed.webp').convert('RGBA'); px = im.load(); w, h = im.size
dark = [(x, y) for y in range(int(h * .45), int(h * .9)) for x in range(int(w * .1), int(w * .9))
        if px[x, y][3] > 200 and sum(px[x, y][:3]) < 200]
xs = sorted(x for x, _ in dark); ys = sorted(y for _, y in dark)
lo = lambda v: v[len(v) // 50]; hi = lambda v: v[-len(v) // 50]
print('window', f'left {lo(xs) / w:.3f} top {lo(ys) / h:.3f} right {hi(xs) / w:.3f} bottom {hi(ys) / h:.3f}')

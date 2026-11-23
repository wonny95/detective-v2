"""The acorn savings jar (user decision 2026-11-23: the word games fill a jar of acorns, spent as notebook hints once a
case's own three are gone). One sheet, Nano Banana 2.1 16:9 2K, job 9f78d2a5-082d-4d88-989d-b619dccb950b, the safe icon
as style reference, flat magenta -> assets/ui/acorn-jar-higgsfield-original.png: empty, half full, full.
Magenta keyed out (as scripts/cut-pablo.py); the three cropped by one box (the union of what is drawn in each third,
in its own coordinates) so the jar sits at the same place in each, 300 px wide -> assets/ui/acorn-jar-0/1/2.webp.
Run from the project folder: python -I scripts/cut-acorn-jar.py"""
from PIL import Image, ImageFilter
src = Image.open('assets/ui/acorn-jar-higgsfield-original.png').convert('RGB')
THIRDS = [38, 946, 1852]; W = 862
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
parts = [key_out(src.crop((x0, 0, x0 + W, src.height))) for x0 in THIRDS]
boxes = [p.getchannel('A').point(lambda a: 255 if a > 24 else 0).getbbox() for p in parts]
box = (min(b[0] for b in boxes) - 10, min(b[1] for b in boxes) - 10, max(b[2] for b in boxes) + 10, max(b[3] for b in boxes) + 10)
for i, p in enumerate(parts):
    im = p.crop(box); im = im.resize((300, round(im.height * 300 / im.width)), Image.LANCZOS)
    im.save(f'assets/ui/acorn-jar-{i}.webp', quality=90)
    print(i, im.size)

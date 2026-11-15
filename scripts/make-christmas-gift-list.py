import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
src = 'assets/places/christmas/gift-list-higgsfield-original.png'
im = Image.open(src).convert('RGBA')
W, H = im.size
px = im.load()
# magenta out (with soft edge and despill)
for y in range(H):
    for x in range(W):
        r, g, b, a = px[x, y]
        mag = min(r, b) - g
        if mag > 90: px[x, y] = (0, 0, 0, 0)
        elif mag > 30:
            k = (mag - 30) / 60
            px[x, y] = (int(r - (r - g) * k * .8), g, int(b - (b - g) * k * .8), int(255 * (1 - k)))
# the paper: cream pixels, bounding box on the middle row/column
def cream(p): r, g, b, a = p; return a > 200 and r > 235 and g > 215 and 170 < b < 225
cy = H * 6 // 10; cx = W // 2
xs = [x for x in range(W) if cream(px[x, cy])]; ys = [y for y in range(H) if cream(px[min(xs) + 60, y])]
L, R, T, B = min(xs), max(xs), min(ys), max(ys)
print('paper', L, T, R, B)
bb = im.getbbox(); print('bbox', bb)
im = im.crop(bb); L -= bb[0]; R -= bb[0]; T -= bb[1]; B -= bb[1]
F = 'C:/Windows/Fonts/Inkfree.ttf'
ink = (63, 51, 38, 255); pencil = (47, 79, 134, 255)
names = ['Lumi', 'Tilly', 'Bo', 'Nori', 'Kit', 'Poppy']
pw = R - L
def make(done, out):
    page = im.copy(); d = ImageDraw.Draw(page)
    x0 = L + pw * .1
    t = ImageFont.truetype(F, int(pw * .085)); s = ImageFont.truetype(F, int(pw * .075)); n = ImageFont.truetype(F, int(pw * .095))
    y = T + (B - T) * .08
    d.text((L + pw / 2, y), 'Gifts for This Delivery', font=t, fill=ink, anchor='mt')
    y += pw * .13
    d.line([(L + pw * .1, y), (R - pw * .1, y)], fill=ink, width=3)
    y += pw * .09
    d.text((x0, y), 'Toy gifts: 6', font=s, fill=ink)
    y += pw * .17
    step = pw * .135
    for i, nm in enumerate(names):
        yy = y + i * step
        # a box to tick
        bx = x0; sz = pw * .07
        d.rectangle([bx, yy + sz * .25, bx + sz, yy + sz * 1.25], outline=ink, width=3)
        if i < done:
            d.line([(bx + sz * .15, yy + sz * .75), (bx + sz * .45, yy + sz * 1.1), (bx + sz * 1.15, yy - sz * .1)], fill=pencil, width=6, joint='curve')
        d.text((bx + sz * 1.7, yy), nm, font=n, fill=ink)
    page.save(out)
    print(out, page.size)
make(2, 'assets/places/christmas/gift-list-2.png')
make(4, 'assets/places/christmas/gift-list-4.png')

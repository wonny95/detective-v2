"""Word matching (user request 2026-11-27): pushpins seen from above and the same pins with the red thread wound round
them, cut from assets/ui/match-pins-higgsfield-original.png (Higgsfield job f10021a8, 16:9 2K).

The background is the white joined to the picture's edge (flood fill), so a white highlight on a pin head stays.
Pieces are found by the gaps between them (rows, then columns in each row).
Writes assets/ui/match/pin.webp, pin-wound-r.webp (thread end to the right), pin-wound-l.webp, thread.webp
Run from the project folder: python -I scripts/cut-match-pins.py   (Pillow only)"""
from PIL import Image, ImageChops, ImageDraw, ImageFilter
import os

SRC = 'assets/ui/match-pins-higgsfield-original.png'
OUT = 'assets/ui/match/'
os.makedirs(OUT, exist_ok=True)
im = Image.open(SRC).convert('RGB')
W, H = im.size

# background = near-white pixels joined to the border
g = im.convert('L')
near = Image.eval(im.split()[0], lambda v: 0)   # placeholder size
px = im.load()
m = Image.new('L', im.size, 0); mp = m.load()
for y in range(H):
    for x in range(W):
        r, gg, b = px[x, y]
        if min(r, gg, b) > 228: mp[x, y] = 255
ImageDraw.floodfill(m, (0, 0), 128)
ImageDraw.floodfill(m, (W - 1, H - 1), 128) if m.getpixel((W - 1, H - 1)) == 255 else None
bg = m.point(lambda v: 255 if v == 128 else 0)
alpha = bg.point(lambda v: 255 - v).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))


def spans(profile, gap, minlen):
    out, start, run = [], None, 0
    for i, v in enumerate(profile):
        if v:
            if start is None: start = i
            run = 0
        elif start is not None:
            run += 1
            if run >= gap:
                if i - run - start >= minlen: out.append((start, i - run + 1))
                start, run = None, 0
    if start is not None: out.append((start, len(profile)))
    return out


fg = alpha.point(lambda v: 1 if v > 40 else 0)
fp = fg.load()
rows = spans([any(fp[x, y] for x in range(0, W, 2)) for y in range(H)], 12, 30)
pieces = []
for (y0, y1) in rows:
    cols = spans([any(fp[x, y] for y in range(y0, y1, 2)) for x in range(W)], 10, 30)
    pieces.append([(x0, y0, x1, y1) for (x0, x1) in cols])
print('rows', [len(r) for r in pieces])

rgba = im.copy(); rgba.putalpha(alpha)


def save(box, name, size):
    c = rgba.crop(box)
    c = c.crop(c.getchannel('A').getbbox())
    k = size / max(c.size)
    c = c.resize((round(c.width * k), round(c.height * k)), Image.LANCZOS)
    c.save(OUT + name + '.webp', quality=92, method=6)
    print(name, c.size)


# (pin.webp is cut below, centred on its head)
save(pieces[1][0], 'pin-wound-r', 160)
save(pieces[1][1], 'pin-wound-l', 160)
save(pieces[2][0], 'thread', 600)

# the plain pin and the wound pin without its loose end (user 2026-11-27: the end pointed one way while the string went
# another and looked broken; then: the pin moved when it was joined). Both are square crops of the sheet at the same
# scale, centred on the pin's round head, so swapping one for the other leaves the head where it was. The wound one is
# cut round (its loose end goes); the string is drawn from under the pin's middle.
def head(box):
    """the middle of the bright red round head (the wound thread is darker, so it is left out)"""
    x0, y0, x1, y1 = box; p = im.load(); xs = ys = n = 0
    for y in range(y0, y1):
        for x in range(x0, x1):
            r_, g_, b_ = p[x, y]
            if r_ > 215 and 70 < g_ < 150 and b_ < 120 and alpha.getpixel((x, y)) > 200: xs += x; ys += y; n += 1
    return xs / n, ys / n


plain, wound = pieces[0][0], pieces[1][0]
R = (plain[2] - plain[0]) / 2 + 6   # the plain pin's disc and a little room
SIZE = 96
for box, name, cut in ((plain, 'pin', False), (wound, 'pin-wound', True)):
    hx, hy = head(box)
    c = rgba.crop((round(hx - R), round(hy - R), round(hx + R), round(hy + R)))
    if cut:
        m = Image.new('L', c.size, 0); ImageDraw.Draw(m).ellipse((4, 4, c.width - 4, c.height - 4), fill=255)
        c.putalpha(ImageChops.multiply(c.getchannel('A'), m.filter(ImageFilter.GaussianBlur(1.5))))
    c = c.resize((SIZE, SIZE), Image.LANCZOS)
    c.save(OUT + name + '.webp', quality=92, method=6)
    print(name, c.size, 'head', round(hx), round(hy))

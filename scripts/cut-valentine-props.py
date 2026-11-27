"""Valentine case (design/case-valentine-chocolate.md, "그림 제작 계획" 6): cut the chocolates and boxes out of the item sheet.

Sheet: assets/places/valentine/choc-sheet-higgsfield-original.png (Higgsfield Nano Banana 2.1 16:9 2K 2752×1536, flat
magenta, job e932dd09-2b97-4500-908a-2398515a3f91). Top-down items (the packing close look, layout B) and one item seen
from the front (desk-boxes, on the classroom desk). The sheet drew a second square chocolate and a second open/closed
gift box pair; those are not cut.

Writes assets/places/valentine/<name>.webp (magenta keyed out, alpha bbox + a small margin, scaled to the size below)
and prints where the four molds of gift-open sit, as fractions of that picture (top-left heart, top-right heart,
bottom-left flower, bottom-right square) for the code that drops a chocolate into its mold.
Magenta is taken out by how far green sits under red and blue (stricter than cut-valentine-characters.py, so the pinks stay).
Run from the project folder: python -I scripts/cut-valentine-props.py   (Pillow only)"""
from PIL import Image, ImageDraw

SRC = 'assets/places/valentine/choc-sheet-higgsfield-original.png'
OUT = 'assets/places/valentine/'
# name: (x0, y0, x1, y1) on the sheet (found by the magenta gaps), longest side after scaling
ITEMS = {
    'choc-pink-heart':  ((112, 88, 512, 448), 176),
    'choc-brown-heart': ((544, 88, 952, 448), 176),
    'choc-flower':      ((984, 80, 1368, 456), 176),
    'choc-square':      ((1408, 88, 1776, 448), 176),
    'bigbox-closed':    ((112, 464, 704, 1024), 720),
    'bigbox-open':      ((736, 464, 1336, 1024), 720),
    'gift-open':        ((1656, 504, 2120, 960), 320),
    'gift-closed':      ((2192, 496, 2648, 960), 320),
    'bag-pink-hearts':  ((1064, 1032, 1376, 1472), 220),
    'bag-flowers':      ((1376, 1032, 1696, 1472), 220),
    'desk-boxes':       ((1664, 976, 2680, 1480), 720),
}


def unmagenta(px):
    # stricter than the character sheets' key: the pinks here (pink heart, ribbons, the gift box rim) have green well
    # above zero, so only colours where green sits far under both red and blue count as magenta
    r, g, b = px
    mag = min(1.0, max(0.0, (min(r, b) - g - 60) / 150))
    al = 1 - mag
    if al <= 0.02:
        return (0, 0, 0, 0)
    un = lambda v, m: int(min(255, max(0, (v - m * (1 - al)) / al)))
    return (un(r, 255), un(g, 0), un(b, 255), int(al * 255))


def largest_only(img, s=4):
    """keep only the biggest blob (a box can catch the edge of the next item): flood fill on a 1/s mask"""
    a = img.getchannel('A').point(lambda v: 255 if v > 40 else 0)
    sm = a.resize((max(1, img.width // s), max(1, img.height // s)), Image.BOX)
    W, H = sm.size; px = sm.load(); lab = [[0] * W for _ in range(H)]; sizes = {}
    n = 0
    for y in range(H):
        for x in range(W):
            if px[x, y] > 0 and not lab[y][x]:
                n += 1; lab[y][x] = n; st = [(x, y)]; c = 0
                while st:
                    cx, cy = st.pop(); c += 1
                    for dx in (-1, 0, 1):
                        for dy in (-1, 0, 1):
                            nx, ny = cx + dx, cy + dy
                            if 0 <= nx < W and 0 <= ny < H and px[nx, ny] > 0 and not lab[ny][nx]:
                                lab[ny][nx] = n; st.append((nx, ny))
                sizes[n] = c
    if len(sizes) < 2:
        return img
    keep = max(sizes, key=sizes.get)
    m = Image.new('L', (W, H)); mp = m.load()
    for y in range(H):
        for x in range(W):
            mp[x, y] = 255 if lab[y][x] == keep else 0
    m = m.resize(img.size, Image.NEAREST)
    out = img.copy(); out.putalpha(Image.composite(img.getchannel('A'), Image.new('L', img.size, 0), m))
    return out


def cut(sheet, box, longest):
    piece = sheet.crop(box)
    out = Image.new('RGBA', piece.size)
    out.putdata([unmagenta(p) for p in piece.getdata()])
    out = largest_only(out)
    out = out.crop(out.getchannel('A').point(lambda v: 255 if v > 40 else 0).getbbox())
    m = max(2, round(max(out.size) * .02))
    pad = Image.new('RGBA', (out.width + 2 * m, out.height + 2 * m))
    pad.paste(out, (m, m))
    k = longest / max(pad.size)
    return pad.resize((round(pad.width * k), round(pad.height * k)), Image.LANCZOS)


def molds(img):
    """the tray inside the pink rim (the brown part), split in four: each mold's centre as fractions of the picture"""
    px = img.load()
    xs, ys = [], []
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = px[x, y]
            if a > 200 and r < 175 and g < 130 and r > g:   # chocolate-brown tray, not the pink rim
                xs.append(x); ys.append(y)
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    cx = [x0 + (x1 - x0) * .25, x0 + (x1 - x0) * .75]
    cy = [y0 + (y1 - y0) * .25, y0 + (y1 - y0) * .75]
    pts = [(cx[0], cy[0]), (cx[1], cy[0]), (cx[0], cy[1]), (cx[1], cy[1])]
    size = (x1 - x0) / 2
    return [(round(x / img.width, 3), round(y / img.height, 3)) for x, y in pts], round(size / img.width, 3)


sheet = Image.open(SRC).convert('RGB')
for name, (box, longest) in ITEMS.items():
    img = cut(sheet, box, longest)
    img.save(OUT + name + '.webp', quality=92)
    print(name, img.size)
    if name == 'gift-open':
        pts, size = molds(img)
        print('  molds (tl heart, tr heart, bl flower, br square):', pts, ' mold cell width:', size)
        dbg = img.copy(); d = ImageDraw.Draw(dbg)
        for fx, fy in pts:
            x, y = fx * img.width, fy * img.height
            d.ellipse((x - 5, y - 5, x + 5, y + 5), fill=(0, 200, 255, 255))
        dbg.save('.preview/gift-open-molds.png')

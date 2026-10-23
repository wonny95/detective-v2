"""Cut the menu icon sheet (assets/ui/nav-icons-higgsfield-original.png, 3x2 on magenta) into
assets/ui/nav/<name>.png: alpha by how magenta a pixel is, magenta taken back out of the edge colours,
each cell cropped to its icon with a 4px square margin and scaled to 160x160."""
from PIL import Image

SRC = 'assets/ui/nav-icons-higgsfield-original.png'
NAMES = [['home-door', 'case-magnifier', 'study-book'], ['my-squirrel', 'my-hat', 'home-door-lantern']]

im = Image.open(SRC).convert('RGB')
W, H = im.size
out = Image.new('RGBA', im.size)
src, dst = im.load(), out.load()
for y in range(H):
    for x in range(W):
        r, g, b = src[x, y]
        k = min(r, b) - g                      # 255 on pure magenta, below 0 on the drawing
        a = 1.0 if k < 60 else 0.0 if k > 200 else (200 - k) / 140
        if a <= 0: dst[x, y] = (0, 0, 0, 0); continue
        if a < 1:                              # un-mix the magenta from the edge
            r = (r - (1 - a) * 255) / a; b = (b - (1 - a) * 255) / a
        dst[x, y] = (max(0, min(255, round(r))), g, max(0, min(255, round(b))), round(a * 255))

for row, names in enumerate(NAMES):
    for col, name in enumerate(names):
        cell = out.crop((col * W // 3, row * H // 2, (col + 1) * W // 3, (row + 1) * H // 2))
        l, t, r, b = cell.getchannel('A').point(lambda v: 255 if v > 24 else 0).getbbox()
        side = max(r - l, b - t) + 8
        sq = Image.new('RGBA', (side, side))
        sq.paste(cell.crop((l, t, r, b)), ((side - (r - l)) // 2, (side - (b - t)) // 2))
        sq.resize((160, 160), Image.LANCZOS).save(f'assets/ui/nav/{name}.png', optimize=True)
        print(name, (r - l, b - t))

"""Cut the menu icon sheets (assets/ui/nav-icons*-higgsfield-original.png, 3x2 on magenta) into
assets/ui/nav/<name>.png: alpha by how magenta a pixel is, magenta taken back out of the edge colours,
each cell cropped to its icon with a 4px square margin and scaled to 160x160."""
from PIL import Image

# a None cell is not used (a candidate the user did not pick)
SHEETS = {
    'assets/ui/nav-icons-higgsfield-original.png': [[None, 'case-magnifier', 'study-book'], [None, 'my-hat', None]],
    'assets/ui/nav-icons-2-higgsfield-original.png': [['home-house', None, None], ['map', 'note', None]],
    'assets/ui/talk-icons-higgsfield-original.png': [[None, None, 'talk'], [None, None, None]],
}

def key(im):
    W, H = im.size
    out = Image.new('RGBA', im.size)
    src, dst = im.load(), out.load()
    for y in range(H):
        for x in range(W):
            r, g, b = src[x, y]
            k = min(r, b) - g                      # 255 on pure magenta, below 0 on the drawing
            a = 1.0 if k < 60 else 0.0 if k > 170 else (170 - k) / 110
            if a <= 0: dst[x, y] = (0, 0, 0, 0); continue
            if a < 1:                              # un-mix the magenta from the edge
                r = (r - (1 - a) * 255) / a; b = (b - (1 - a) * 255) / a
            dst[x, y] = (max(0, min(255, round(r))), g, max(0, min(255, round(b))), round(a * 255))
    return out

for path, names in SHEETS.items():
    out = key(Image.open(path).convert('RGB'))
    W, H = out.size
    for row, cells in enumerate(names):
        for col, name in enumerate(cells):
            if not name: continue
            cell = out.crop((col * W // 3, row * H // 2, (col + 1) * W // 3, (row + 1) * H // 2))
            l, t, r, b = cell.getchannel('A').point(lambda v: 255 if v > 64 else 0).getbbox()
            side = max(r - l, b - t) + 8
            sq = Image.new('RGBA', (side, side))
            sq.paste(cell.crop((l, t, r, b)), ((side - (r - l)) // 2, (side - (b - t)) // 2))
            sq.resize((160, 160), Image.LANCZOS).save(f'assets/ui/nav/{name}.png', optimize=True)
            print(name, (r - l, b - t))

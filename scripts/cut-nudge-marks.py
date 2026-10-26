"""Cut the nudge mark (assets/ui/nudge-bang-higgsfield-original.png, six exclamation marks 3x2 on magenta; the user
picked the second, the ! in a cream speech bubble) into assets/ui/nudge-bang.png: alpha by how magenta a pixel is
(as cut-nav-icons.py), cropped to the drawing with a 4px margin, the longer side 200px."""
from PIL import Image

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

out = key(Image.open('assets/ui/nudge-bang-higgsfield-original.png').convert('RGB'))
W, H = out.size
cell = out.crop((W // 3, 0, 2 * W // 3, H // 2))          # top row, middle cell
l, t, r, b = cell.getchannel('A').point(lambda v: 255 if v > 64 else 0).getbbox()
part = cell.crop((max(0, l - 4), max(0, t - 4), r + 4, b + 4))
s = 200 / max(part.size)
part = part.resize((round(part.width * s), round(part.height * s)), Image.LANCZOS)
part.save('assets/ui/nudge-bang.png', optimize=True)
print('nudge-bang', part.size)

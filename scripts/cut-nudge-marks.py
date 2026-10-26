"""Cut the nudge mark sheets (assets/ui/nudge-bang/-arrow-higgsfield-original.png, 3x2 on magenta) into
assets/ui/nudge/bang-1..6.png and arrow-1..6.png: alpha by how magenta a pixel is (as cut-nav-icons.py), each cell
cropped to its drawing with a 4px margin and scaled so its longer side is 200px."""
import os
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

os.makedirs('assets/ui/nudge', exist_ok=True)
for kind in ('bang', 'arrow'):
    out = key(Image.open(f'assets/ui/nudge-{kind}-higgsfield-original.png').convert('RGB'))
    W, H = out.size
    for i in range(6):
        col, row = i % 3, i // 3
        cell = out.crop((col * W // 3, row * H // 2, (col + 1) * W // 3, (row + 1) * H // 2))
        l, t, r, b = cell.getchannel('A').point(lambda v: 255 if v > 64 else 0).getbbox()
        part = cell.crop((max(0, l - 4), max(0, t - 4), r + 4, b + 4))
        s = 200 / max(part.size)
        part = part.resize((round(part.width * s), round(part.height * s)), Image.LANCZOS)
        part.save(f'assets/ui/nudge/{kind}-{i + 1}.png', optimize=True)
        print(kind, i + 1, part.size)

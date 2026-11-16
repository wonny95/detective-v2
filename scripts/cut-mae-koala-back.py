"""May (koala) from behind at the lighting: the Higgsfield picture on white
(assets/characters/mae-koala-back-higgsfield-original.png) drew her standing on a stool, as the mouse's back view did;
outdoors she stands on the snow (user: not on a stool outside), so the stool is cut away under her feet. White flooded
in from the edges, trimmed, 700 px high -> assets/characters/mae-back.png. Pillow only.
usage: python scripts/cut-mae-koala-back.py"""
from PIL import Image, ImageDraw, ImageFilter
src = Image.open('assets/characters/mae-koala-back-higgsfield-original.png').convert('RGB')
W, H = src.size; MARK = (255, 0, 255)
work = src.copy()
for p in [(x, 0) for x in range(0, W, 6)] + [(x, H - 1) for x in range(0, W, 6)] + [(0, y) for y in range(0, H, 6)] + [(W - 1, y) for y in range(0, H, 6)]:
    c = work.getpixel(p)
    if c != MARK and min(c) > 225: ImageDraw.floodfill(work, p, MARK, thresh=40)
SEAT, SOLE = 848, 890          # the stool's seat shows from SEAT; her soles end at SOLE
FEET = [(372, 446), (484, 560)]  # the columns of her two feet
px, sp = work.load(), src.load()
alpha = Image.new('L', (W, H), 255); ap = alpha.load()
for y in range(H):
    for x in range(W):
        if px[x, y] == MARK: ap[x, y] = 0; continue
        if y >= SOLE: ap[x, y] = 0; continue
        if y >= SEAT - 50 and min(sp[x, y]) > 232: ap[x, y] = 0; continue   # the white gap between her legs
        if y >= SEAT:
            r, g, b = sp[x, y]
            infoot = any(a <= x < c for a, c in FEET)
            if not infoot or (r > 110 and b < .5 * r): ap[x, y] = 0
alpha = alpha.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(.7))
out = src.convert('RGBA'); out.putalpha(alpha)
out = out.crop(alpha.point(lambda v: 255 if v > 40 else 0).getbbox())
m = int(max(out.size) * .03); pad = Image.new('RGBA', (out.width + 2 * m, out.height + 2 * m), (0, 0, 0, 0)); pad.paste(out, (m, m))
pad = pad.resize((round(pad.width * 700 / pad.height), 700), Image.LANCZOS)
pad.save('assets/characters/mae-back.png', optimize=True); print(pad.size)

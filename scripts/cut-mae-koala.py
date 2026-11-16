"""May as a koala (user decision: the mouse looked like the moles from earlier cases, so Nico stood out): one
Higgsfield sheet on white (assets/characters/mae-koala-sheet-higgsfield-original.png; in use the user's own edit of it,
mae-koala-sheet-user-original.png, where the working pose's skirt is purple instead of white) with her working pose (left,
cutting a snowflake) and her talking pose (right, facing the detective). The white is flooded in from the edges, the
closed white gaps below the seat (between the stool legs) are cleared too, each figure is cut by its columns, trimmed
and scaled to 700 px high -> assets/characters/mae-higgsfield.png (work) and mae-talk.png (talk). Pillow only.
usage: python scripts/cut-mae-koala.py"""
from PIL import Image, ImageDraw, ImageFilter
src = Image.open('assets/characters/mae-koala-sheet-user-original.png').convert('RGB')
W, H = src.size
MARK = (255, 0, 255)
work = src.copy()
edge = [(x, 0) for x in range(0, W, 6)] + [(x, H - 1) for x in range(0, W, 6)] + [(0, y) for y in range(0, H, 6)] + [(W - 1, y) for y in range(0, H, 6)]
for p in edge:
    c = work.getpixel(p)
    if c != MARK and min(c) > 225: ImageDraw.floodfill(work, p, MARK, thresh=40)
SEAT = int(H * .78)   # below this only stool legs, feet and the hem: any pure white there is background
px, sp = work.load(), src.load()
for y in range(SEAT, H):
    for x in range(W):
        r, g, b = sp[x, y]
        if px[x, y] != MARK and min(r, g, b) > 232 and max(r, g, b) - min(r, g, b) < 14:
            ImageDraw.floodfill(work, (x, y), MARK, thresh=30)
bg = Image.new('L', (W, H), 0); mp = bg.load()
for y in range(H):
    for x in range(W):
        if px[x, y] == MARK: mp[x, y] = 255
alpha = bg.point(lambda v: 255 - v).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(.7))
sheet = src.convert('RGBA'); sheet.putalpha(alpha)
# split into the two figures by empty columns
cols = [alpha.crop((x, 0, x + 1, H)).getbbox() is not None for x in range(W)]
runs, start = [], None
for x, f in enumerate(cols + [False]):
    if f and start is None: start = x
    if not f and start is not None:
        if x - start > 40: runs.append((start, x))
        start = None
assert len(runs) == 2, runs
for (x0, x1), name in zip(runs, ['mae-higgsfield', 'mae-talk']):
    fig = sheet.crop((x0, 0, x1, H)); fig = fig.crop(fig.getchannel('A').point(lambda v: 255 if v > 40 else 0).getbbox())
    m = int(max(fig.size) * .03); pad = Image.new('RGBA', (fig.width + 2 * m, fig.height + 2 * m), (0, 0, 0, 0)); pad.paste(fig, (m, m))
    pad = pad.resize((round(pad.width * 700 / pad.height), 700), Image.LANCZOS)
    pad.save(f'assets/characters/{name}.png', optimize=True); print(name, pad.size)

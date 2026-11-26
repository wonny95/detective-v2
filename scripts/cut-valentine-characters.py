"""Valentine case (design/case-valentine-chocolate.md, "그림 제작 계획" 3): cut Penny and Suzy out of their character sheets.

Sheets (Higgsfield Nano Banana 2.1 16:9 2K, flat magenta, one character each; user 2026-11-26: idle pose, front view
and talking mouth on one sheet):
- assets/characters/penny-sheet-v3-higgsfield-original.png  job 3b472452-1956-4a6e-b109-42dfb01a5572
- assets/characters/suzy-sheet-higgsfield-original.png      job 42cdfad8-da45-443a-a836-95a37cd609f1
Each sheet: left = the idle pose (`<id>:work`, before the detective talks to her), middle = the front view (talk),
right = two round mouth patches (top closed, bottom open).

Writes assets/characters/<id>-work.webp, <id>-higgsfield.webp (alpha bbox + 3% margin, 700 tall) and
assets/characters/mouths/<id>-patch-closed.png, <id>-patch-open.png (the round patches as drawn, for the mouth step).
Magenta is taken out by how magenta a pixel is, and its tint pulled out of the edges (as cut-case-page-folder.py).
Run from the project folder: python -I scripts/cut-valentine-characters.py   (Pillow only)"""
from PIL import Image

D = 'assets/characters/'
SHEETS = {'penny': D + 'penny-sheet-v3-higgsfield-original.png', 'suzy': D + 'suzy-sheet-higgsfield-original.png'}
H = 700


def unmagenta(px):
    r, g, b = px
    mag = min(1.0, max(0.0, ((r + b) / 2 - g - 40) / 140))
    al = 1 - mag
    if al <= 0.02:
        return (0, 0, 0, 0)
    un = lambda v, m: int(min(255, max(0, (v - m * (1 - al)) / al)))
    return (un(r, 255), un(g, 0), un(b, 255), int(al * 255))


def keyed(path):
    im = Image.open(path).convert('RGB')
    out = Image.new('RGBA', im.size)
    out.putdata([unmagenta(p) for p in im.getdata()])
    return out


def runs(profile, min_gap=12):
    """[start, end) spans where the profile is non-zero, joined across gaps shorter than min_gap"""
    spans, start, gap = [], None, 0
    for i, v in enumerate(profile + [0] * min_gap):
        if v:
            if start is None: start = i
            gap = 0
        elif start is not None:
            gap += 1
            if gap >= min_gap:
                spans.append((start, i - gap + 1)); start, gap = None, 0
    return spans


def solid(a):
    return a.point(lambda v: 255 if v > 40 else 0)


def margin_crop(img):
    box = solid(img.getchannel('A')).getbbox()
    piece = img.crop(box)
    m = round(piece.height * .03)
    out = Image.new('RGBA', (piece.width + 2 * m, piece.height + 2 * m))
    out.paste(piece, (m, m))
    return out


for cid, path in SHEETS.items():
    sheet = keyed(path)
    a = solid(sheet.getchannel('A'))
    w, h = a.size
    px = a.load()
    cols = [sum(1 for y in range(0, h, 4) if px[x, y]) for x in range(w)]
    parts = [s for s in runs(cols, 20) if s[1] - s[0] > 60]
    assert len(parts) == 3, (cid, parts)
    for name, (x0, x1) in zip(('work', 'higgsfield'), parts[:2]):
        fig = margin_crop(sheet.crop((x0, 0, x1, h)))
        fig = fig.resize((round(fig.width * H / fig.height), H), Image.LANCZOS)
        fig.save(f'{D}{cid}-{name}.webp', quality=92)
        print(f'{cid}-{name}.webp', fig.size)
    x0, x1 = parts[2]
    col = a.crop((x0, 0, x1, h)); cp = col.load()
    rows = [sum(1 for x in range(0, x1 - x0, 4) if cp[x, y]) for y in range(h)]
    pats = [s for s in runs(rows, 20) if s[1] - s[0] > 60]
    assert len(pats) == 2, (cid, pats)
    for state, (y0, y1) in zip(('closed', 'open'), pats):
        patch = sheet.crop((x0, y0, x1, y1))
        patch = patch.crop(solid(patch.getchannel('A')).getbbox())
        patch.save(f'{D}mouths/{cid}-patch-{state}.png')
        print(f'mouths/{cid}-patch-{state}.png', patch.size)

# The moods (user request 2026-11-26: one sheet for both, only the faces the front view can't carry):
# assets/characters/valentine-moods-higgsfield-original.png, job adf3df4b-f4f2-44f1-afc8-90c1d2fe3ad8, the two sheets
# above as reference. Left Penny worried (hand on cheek, t0-t2), middle Suzy sorry (ears down, after the order note),
# right two open-mouth patches stacked (Penny's on top). -> penny-worried.webp, suzy-sorry.webp (700 tall),
# mouths/penny-worried-patch-open.png, suzy-sorry-patch-open.png
sheet = keyed(D + 'valentine-moods-higgsfield-original.png')
a = solid(sheet.getchannel('A')); w, h = a.size; px = a.load()
cols = [sum(1 for y in range(0, h, 4) if px[x, y]) for x in range(w)]
parts = [s for s in runs(cols, 20) if s[1] - s[0] > 60]
assert len(parts) == 3, parts
for name, (x0, x1) in zip(('penny-worried', 'suzy-sorry'), parts[:2]):
    fig = margin_crop(sheet.crop((x0, 0, x1, h)))
    fig = fig.resize((round(fig.width * H / fig.height), H), Image.LANCZOS)
    fig.save(f'{D}{name}.webp', quality=92)
    print(f'{name}.webp', fig.size)
x0, x1 = parts[2]
col = a.crop((x0, 0, x1, h)); cp = col.load()
rows = [sum(1 for x in range(0, x1 - x0, 4) if cp[x, y]) for y in range(h)]
pats = [s for s in runs(rows, 20) if s[1] - s[0] > 60]
assert len(pats) == 2, pats
for name, (y0, y1) in zip(('penny-worried', 'suzy-sorry'), pats):
    patch = sheet.crop((x0, y0, x1, y1))
    patch = patch.crop(solid(patch.getchannel('A')).getbbox())
    patch.save(f'{D}mouths/{name}-patch-open.png')
    print(f'mouths/{name}-patch-open.png', patch.size)

"""Coco's and Nico's open mouths (user report 2026-11-16: they looked like a picture laid on top). The closed mouths stay
the drawing as it is; only the open ones are made again, over the same boxes as before (MOUTHS in index.html), and only
the pixels that change are laid on (edges softened), so no box shows.
- Coco (mae): the drawn smile under the nose is painted over with her muzzle's cream (the nose and the short line
  under it stay), and an open smile is drawn in its place (dark inside, pink tongue, the drawing's brown line).
- Nico: the beak parts along its own drawn middle line: the lower beak (its orange and outline under the line, down to
  the white face) drops 3 px, and where it was shows the dark inside of the beak.
Run from the project folder."""
from PIL import Image, ImageChops, ImageDraw, ImageFilter
import math

D = 'assets/characters/'; M = D + 'mouths/'
lum = lambda p: (p[0] * 299 + p[1] * 587 + p[2] * 114) // 1000

def lay(base, new, path):
    """only the changed pixels of new, softened at their edge"""
    d = ImageChops.difference(base.convert('RGB'), new.convert('RGB')).convert('L')
    a = d.point(lambda v: 255 if v > 6 else 0).filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.GaussianBlur(.7))
    out = new.copy(); out.putalpha(ImageChops.multiply(a, base.getchannel('A'))); out.save(path, optimize=True)

def coco():
    x, y, w, h = 167, 238, 78, 31
    base = Image.open(D + 'mae-talk.png').convert('RGBA').crop((x, y, x + w, y + h))
    b = base.load(); new = base.copy(); n = new.load()
    cream = (238, 232, 214, 255)
    # paint over the smile: dark and mid pixels from row 5 down, except the line under the nose (x 30..37) to row 8
    hole = Image.new('L', (w, h)); hp = hole.load()
    for j in range(5, h):
        for i in range(w):
            if lum(b[i, j]) < 205 and not (30 <= i <= 37 and j <= 8): hp[i, j] = 255
    hole = hole.filter(ImageFilter.MaxFilter(3)); hp = hole.load()
    for j in range(h):
        for i in range(w):
            if hp[i, j]: n[i, j] = cream
    # the open smile, drawn 4x and scaled down: from x 19 to 57, top at row 9 (under the nose line), round bottom
    k = 4; big = Image.new('RGBA', (w * k, h * k), (0, 0, 0, 0)); g = ImageDraw.Draw(big)
    L, R, T, B = 19 * k, 57 * k, 9 * k, 23 * k
    top = [(L + (R - L) * t / 20, T + 1.5 * k * math.sin(math.pi * t / 20) * 0) for t in range(21)]
    bottom = [(L + (R - L) * (1 - t / 20), T + (B - T) * math.sin(math.pi * (1 - t / 20))) for t in range(21)]
    shape = top + bottom
    g.polygon(shape, fill=(118, 44, 46, 255))
    g.ellipse((L + (R - L) * .28, T + (B - T) * .52, L + (R - L) * .72, B + 2.5 * k), fill=(232, 136, 146, 255))
    clip = Image.new('L', big.size); ImageDraw.Draw(clip).polygon(shape, fill=255)
    big.putalpha(ImageChops.multiply(big.getchannel('A'), clip))
    ImageDraw.Draw(big).line(shape + [shape[0]], fill=(84, 48, 40, 255), width=int(2.4 * k), joint='curve')
    new.alpha_composite(big.resize((w, h), Image.LANCZOS))
    lay(base, new, M + 'mae-open.png')

def nico(box=(170, 176, 238, 214), rows=(15, 24), gap=3):   # 4 px taller than the closed box: room for the drop
    base = Image.open(D + 'nico-higgsfield.png').convert('RGBA').crop(box); W, H = base.size; b = base.load()
    # the beak's middle line: in each column the lowest dark pixel of the dark run inside rows 15..24
    line = {}
    for i in range(W):
        dark = [j for j in range(rows[0], rows[1]) if b[i, j][3] > 200 and lum(b[i, j]) < 90]
        if dark: line[i] = max(dark)
    # the lower beak: under the line, its orange and its outline, down to the white face
    low = Image.new('L', (W, H)); lp = low.load(); ends = (min(line) + 7, max(line) - 7)   # not the beak's tips
    for i, l in line.items():
        if not ends[0] <= i <= ends[1]: continue
        for j in range(l + 1, H):
            r, g_, bl, a = b[i, j]
            if a < 200 or (lum(b[i, j]) > 200 and max(r, g_, bl) - min(r, g_, bl) < 40): break   # the white face
            lp[i, j] = 255
    layer = base.copy(); layer.putalpha(low)
    new = base.copy(); n = new.load()
    for i in range(W):   # where the lower beak was: the dark inside of the beak
        for j in range(H):
            if lp[i, j]: n[i, j] = (112, 40, 42, 255)
    new.alpha_composite(layer, (0, gap))   # the lower beak, dropped
    lay(base, new, M + 'nico-open.png')

coco(); nico()
print('ok')

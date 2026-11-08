"""Violin case people from the Higgsfield sheets, background removed by Higgsfield (remove_background, job ids in
assets/characters/README.md; the cut-outs are kept outside the repo, folder given as the first argument, files
<sheet>-cutout.png): Tara (left) and Owen (right), Momo (left) and Pip (right), Ivo alone, Owen nervous, Owen sad (the
left one of the two drawn). Same crop, size and face icon as scripts/cut-umbrella-characters.py: a 3% margin, 700 px
tall -> assets/characters/<id>-higgsfield.png, and a 160 px face icon -> assets/ui/icons-v2/<id>.png.
These sheets kept the drawings' white sticker rim after the background removal: it is peeled off from the outside in,
only light and greyish pixels, stopping at the brown ink outline (as the mole/fox/raccoon/rabbit rim, 2026-10-16).
Prints each sprite's size and the face viewBox for SPRITES.
Run from the project folder: python -I scripts/cut-violin-characters.py <cut-out folder>"""
import sys
from collections import deque
from PIL import Image, ImageFilter, ImageDraw, ImageChops
D = 'assets/characters/'
CUT = sys.argv[1].rstrip('/\\') + '/'
def trim(im):
    box = im.getchannel('A').point(lambda a: 255 if a > 24 else 0).getbbox()
    im = im.crop(box); m = round(max(im.size) * .03)
    out = Image.new('RGBA', (im.width + 2 * m, im.height + 2 * m)); out.paste(im, (m, m)); return out
def solid(cut, orig):
    a = cut.getchannel('A'); out = a.point(lambda v: 255 if v > 24 else 0); ImageDraw.floodfill(out, (0, 0), 128)
    inside = out.point(lambda v: 0 if v == 128 else 255).filter(ImageFilter.MinFilter(5))   # the soft outer edge stays
    weak = ImageChops.multiply(inside, a.point(lambda v: 255 if v < 250 else 0))
    cut.paste(orig.convert('RGBA'), (0, 0), weak); return cut
def peel(im, reach=36):
    """the sticker rim: light (>= 200), greyish (spread < 46) pixels reached from the clear outside, at most `reach` px in"""
    W, H = im.size; px = im.load(); data = list(im.get_flattened_data())
    rim = lambda p: p[3] > 24 and min(p[:3]) >= 200 - (255 - p[3]) // 2 and max(p[:3]) - min(p[:3]) < 46
    dist = bytearray(W * H); seen = bytearray(W * H); q = deque()
    # start from the clear pixels that touch the drawing
    for i, p in enumerate(data):
        if p[3] <= 24:
            seen[i] = 1; x, y = i % W, i // W
            if (x + 1 < W and data[i + 1][3] > 24) or (x and data[i - 1][3] > 24) or (y + 1 < H and data[i + W][3] > 24) or (y and data[i - W][3] > 24):
                q.append(i)
    gone = []
    while q:
        i = q.popleft(); d = dist[i]
        if d >= reach: continue
        x, y = i % W, i // W
        for j, ok in ((i + 1, x + 1 < W), (i - 1, x > 0), (i + W, y + 1 < H), (i - W, y > 0)):
            if ok and not seen[j] and rim(data[j]):
                seen[j] = 1; dist[j] = d + 1; q.append(j); gone.append(j)
    for j in gone:
        r, g, b, _ = data[j]; px[j % W, j // W] = (r, g, b, 0)
    # a 1 px soft edge against the ink, as the drawing's own outer edge
    a = im.getchannel('A'); im.putalpha(ImageChops.multiply(a, a.filter(ImageFilter.GaussianBlur(.7)).point(lambda v: min(255, v * 2))))
    return im
def square(im, cx, y0, side):
    face = Image.new('RGBA', (side, side)); face.paste(im.crop((round(cx - side / 2), y0, round(cx + side / 2), y0 + side)), (0, 0))
    return face
def save(id, im, head):
    """head: (centre x, top, side) as shares of the sprite's width/height; None: no face icon (an expression)"""
    im = trim(im); s = 700 / im.height
    im = im.resize((round(im.width * s), 700), Image.LANCZOS)
    im.save(D + f'{id}-higgsfield.png', optimize=True)
    if not head: return print(id, im.size)
    W, H = im.size; x, y, z = head; cx, y0, side = round(x * W), round(y * H), round(z * H)
    print(id, im.size, f"face:'{round(cx - side / 2)} {y0} {side} {side}'")
    icon = Image.new('RGBA', (160, 160)); icon.paste(square(im, cx, y0, side).resize((148, 148), Image.LANCZOS), (6, 6))
    rim = icon.getchannel('A').point(lambda v: 255 if v > 40 else 0).filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.GaussianBlur(.8))
    white = Image.new('RGBA', (160, 160), (255, 255, 255, 255)); white.putalpha(rim)
    white.alpha_composite(icon); white.save(f'assets/ui/icons-v2/{id}.png', optimize=True)
def sheet(name, orig):
    return peel(solid(Image.open(CUT + f'{name}-cutout.png').convert('RGBA'), Image.open(D + orig)))
for name, orig, parts in [
        ('tara-owen', 'tara-owen-higgsfield-original.jpg', [('tara', 0, .5, (.5, .02, .5)), ('owen', .5, 1, (.42, .0, .5))]),
        ('momo-pip', 'momo-pip-higgsfield-original.jpg', [('momo', 0, .5, (.5, .02, .5)), ('pip', .5, 1, (.5, .0, .62))]),
        ('ivo', 'ivo-higgsfield-original.jpg', [('ivo', 0, 1, (.5, .0, .52))]),
        ('owen-nervous', 'owen-nervous-original.jpg', [('owen-nervous', 0, 1, None)]),
        ('owen-sad', 'owen-sad-original.jpg', [('owen-sad', 0, .5, None)])]:
    im = sheet(name, orig)
    for id, x0, x1, head in parts:
        save(id, im.crop((round(im.width * x0), 0, round(im.width * x1), im.height)), head)

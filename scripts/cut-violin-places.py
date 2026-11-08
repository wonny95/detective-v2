"""Violin case places and things (assets/places/violin/), as scripts/cut-umbrella-places.py:
- each place drawn as one tall Higgsfield picture with its floor: scaled to 1376 wide, a 1376x768 band from TOP is the
  place picture (<id>.jpg), everything under it the conversation floor (<id>-floor.jpg, ART_FLOOR). The lobby's band
  starts low enough that the leaflet under the bench is in it; the backstage's (and its open-curtain picture's) that the
  floor in front of the curtain is.
- the things carried (case closed and open, button, cutters): cut from the background-removed item sheet
  (remove_background, kept outside the repo: first argument, items-cutout.png), the white sticker rim peeled off as the
  people's (scripts/cut-violin-characters.py), a 3% margin.
- the sleeves: each panel of the sleeves sheet, the paper cleared from its edges in (light greyish pixels, stopping at
  the ink), so the cuffs alone go over the room in the close look (as the umbrella's, user request: no paper).
- Tara's photo of her case, 1024 wide.
- the map: the music hall's part of the edited map pasted on the day map (village-map-day-higgsfield.webp), edges
  blended, as the umbrella case's buildings.
Run from the project folder: python -I scripts/cut-violin-places.py <cut-out folder>"""
import sys
from array import array
from collections import deque
from PIL import Image, ImageFilter, ImageChops, ImageDraw
D = 'assets/places/violin/'
CUT = sys.argv[1].rstrip('/\\') + '/'
TOP = {'lobby': 380, 'waiting': 140, 'stage': 160, 'backstage': 250, 'backstage-open': 250}
for id, top in TOP.items():
    im = Image.open(D + f'{id}-higgsfield-original.jpg').convert('RGB').resize((1376, 1843), Image.LANCZOS)
    im.crop((0, top, 1376, top + 768)).save(D + f'{id}.jpg', quality=88)
    if id != 'backstage-open':
        floor = im.crop((0, top + 768, 1376, 1843)); floor.save(D + f'{id}-floor.jpg', quality=85)
        print(id, 'floor h', floor.height)

def clear(im, seeds, reach):
    """light (>= 200), greyish (spread < 46) pixels reached from the seeds, at most `reach` px in, become clear"""
    W, H = im.size; data = list(im.get_flattened_data()); px = im.load()
    rim = lambda p: p[3] > 24 and min(p[:3]) >= 200 - (255 - p[3]) // 2 and max(p[:3]) - min(p[:3]) < 46
    dist = array("H", bytes(2 * W * H)); seen = bytearray(W * H); q = deque()
    for i in seeds(data, W, H): seen[i] = 1; q.append(i)
    gone = []
    while q:
        i = q.popleft(); d = dist[i]
        if d >= reach: continue
        x, y = i % W, i // W
        for j, ok in ((i + 1, x + 1 < W), (i - 1, x > 0), (i + W, y + 1 < H), (i - W, y > 0)):
            if ok and not seen[j] and rim(data[j]):
                seen[j] = 1; dist[j] = d + 1; q.append(j); gone.append(j)
    for i in seeds(data, W, H):
        if rim(data[i]): gone.append(i)
    for j in gone:
        r, g, b, _ = data[j]; px[j % W, j // W] = (r, g, b, 0)
    a = im.getchannel('A'); im.putalpha(ImageChops.multiply(a, a.filter(ImageFilter.GaussianBlur(.7)).point(lambda v: min(255, v * 2))))
    return im
def outside(data, W, H):   # the clear pixels that touch the drawing
    for i, p in enumerate(data):
        if p[3] <= 24:
            x, y = i % W, i // W
            if (x + 1 < W and data[i + 1][3] > 24) or (x and data[i - 1][3] > 24) or (y + 1 < H and data[i + W][3] > 24) or (y and data[i - W][3] > 24):
                yield i
def edges(data, W, H):     # the picture's four edges
    yield from range(W); yield from range(W * (H - 1), W * H)
    for y in range(1, H - 1): yield y * W; yield y * W + W - 1
def big(im, share=.05):
    """only the large pieces stay (the cuffs): specks of the paper's grain left on their own become clear"""
    W, H = im.size; a = list(im.getchannel('A').get_flattened_data()); seen = bytearray(W * H); parts = []
    for s in range(W * H):
        if a[s] <= 24 or seen[s]: continue
        seen[s] = 1; q = deque([s]); part = []
        while q:
            i = q.popleft(); part.append(i); x, y = i % W, i // W
            for j, ok in ((i + 1, x + 1 < W), (i - 1, x > 0), (i + W, y + 1 < H), (i - W, y > 0)):
                if ok and not seen[j] and a[j] > 24: seen[j] = 1; q.append(j)
        parts.append(part)
    most = max(len(p) for p in parts); px = im.load()
    for p in parts:
        if len(p) < most * share:
            for i in p: r, g, b, _ = px[i % W, i // W]; px[i % W, i // W] = (r, g, b, 0)
    return im
def trim(im):
    box = im.getchannel('A').point(lambda a: 255 if a > 24 else 0).getbbox()
    im = im.crop(box); m = round(max(im.size) * .03)
    out = Image.new('RGBA', (im.width + 2 * m, im.height + 2 * m)); out.paste(im, (m, m)); return out

items = clear(Image.open(CUT + 'items-cutout.png').convert('RGBA'), outside, 36)
for id, x0, x1, h in [('case-closed', 150, 684, 640), ('case-open', 790, 1581, 640), ('gold-button', 1624, 2051, 240), ('cutters', 2115, 2607, 460)]:
    t = trim(items.crop((x0, 0, x1, items.height))); w = round(t.width * h / t.height)
    t.resize((w, h), Image.LANCZOS).save(D + f'{id}.png', optimize=True); print(id, (w, h))

# the sleeves sheet's panels, inside their pencil frames; 300 px tall each
sheet = Image.open(D + 'sleeves-sheet-original.jpg').convert('RGBA')
for id, x, y in [('sleeves-owen', 100, 90), ('sleeves-ivo', 1446, 90), ('sleeves-momo', 100, 820)]:
    t = trim(big(clear(sheet.crop((x, y, x + 1208, y + 626)), edges, 400))); w = round(t.width * 300 / t.height)
    t.resize((w, 300), Image.LANCZOS).save(D + f'{id}.png', optimize=True); print(id, (w, 300))

Image.open(D + 'tara-photo-higgsfield-original.jpg').convert('RGB').resize((1024, 765), Image.LANCZOS).save(D + 'tara-photo.jpg', quality=88)

# the map: where the edit differs from the day map (the music hall and its path), with a blended edge
day = Image.open('assets/places/village-map-day-higgsfield.webp').convert('RGB')
ed = Image.open('assets/places/map-violin-higgsfield-original.jpg').convert('RGB').resize(day.size, Image.LANCZOS)
box = (540, 410, 768, 610)
hit = ImageChops.difference(day.crop(box), ed.crop(box)).convert('L').point(lambda v: 255 if v > 45 else 0)
mask = Image.new('L', day.size, 0); mask.paste(hit.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(4)), box[:2])
day.paste(ed, (0, 0), mask); day.save('assets/places/village-map-day-higgsfield.webp', quality=90); print('map', day.size)

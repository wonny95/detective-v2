"""Christmas case: the gold star as a tree-topper (user request: not a flat cookie star) and no white sticker border.
- The three Higgsfield pictures on flat grey (star-front / star-back / box-star -higgsfield-original.png) are cut out:
  the grey joined to the picture's edge goes, its soft edge fades by how far a pixel is from the grey (the colour
  pulled off the grey so no grey fringe stays), then each is fitted into the old picture's size so the game's frames
  and photo crops stay.
- toy-star-back.png keeps its drawing; only the white border around it is taken away (whitish pixels joined to the
  outside, and the light fringe next to them).
Run from the project folder."""
from PIL import Image, ImageChops, ImageDraw

D = 'assets/places/christmas/'

def flood_outside(mask):
    """mask: L image, 255 where the pixel may belong to the outside; returns the part joined to the picture's edge"""
    m = mask.copy(); W, H = m.size
    for x in range(W):
        for y in (0, H - 1):
            if m.getpixel((x, y)) == 255: ImageDraw.floodfill(m, (x, y), 128)
    for y in range(H):
        for x in (0, W - 1):
            if m.getpixel((x, y)) == 255: ImageDraw.floodfill(m, (x, y), 128)
    return m.point(lambda v: 255 if v == 128 else 0)

def cut_grey(src, size):
    im = Image.open(D + src).convert('RGB'); W, H = im.size
    bg = im.getpixel((4, 4))
    dist = ImageChops.difference(im, Image.new('RGB', im.size, bg))
    r, g, b = dist.split(); dist = ImageChops.lighter(ImageChops.lighter(r, g), b)
    outside = flood_outside(dist.point(lambda v: 255 if v < 45 else 0))
    # one more pixel round the outside, so its soft edge is faded too
    from PIL import ImageFilter
    near = outside.filter(ImageFilter.MaxFilter(3))
    s, dv, nv = im.load(), dist.load(), near.load()
    out = Image.new('RGBA', im.size); o = out.load()
    for y in range(H):
        for x in range(W):
            c = s[x, y]
            if not nv[x, y]: o[x, y] = c + (255,); continue
            a = min(1.0, max(0.0, (dv[x, y] - 8) / 37))
            if a <= 0: o[x, y] = (0, 0, 0, 0); continue
            o[x, y] = tuple(max(0, min(255, round((c[i] - (1 - a) * bg[i]) / a))) for i in range(3)) + (round(a * 255),)
    out = out.crop(out.getchannel('A').point(lambda v: 255 if v > 24 else 0).getbbox())
    k = min(size[0] / out.width, size[1] / out.height)
    out = out.resize((round(out.width * k), round(out.height * k)), Image.LANCZOS)
    canvas = Image.new('RGBA', size); canvas.alpha_composite(out, ((size[0] - out.width) // 2, (size[1] - out.height) // 2))
    return canvas

def strip_white_border(path):
    im = Image.open(D + path).convert('RGBA'); W, H = im.size; p = im.load()
    may = Image.new('L', im.size); m = may.load()
    for y in range(H):
        for x in range(W):
            r, g, b, a = p[x, y]
            if a < 40 or (max(r, g, b) - min(r, g, b) < 45 and (min(r, g, b) > 110 or (a < 200 and min(r, g, b) > 60))): m[x, y] = 255   # white, and the grey of its own soft edge
    gone = flood_outside(may)
    from PIL import ImageFilter
    ring = ImageChops.subtract(gone.filter(ImageFilter.MaxFilter(5)), gone)
    gv, rv = gone.load(), ring.load()
    for y in range(H):
        for x in range(W):
            if gv[x, y]: p[x, y] = (0, 0, 0, 0); continue
            if rv[x, y]:
                r, g, b, a = p[x, y]; light = min(r, g, b)
                if light > 150:   # the light fringe between the white border and the drawing's own outline
                    k = max(0.0, (225 - light) / 75); p[x, y] = (r, g, b, round(a * k))
    im = im.crop(im.getchannel('A').point(lambda v: 255 if v > 24 else 0).getbbox())
    canvas = Image.new('RGBA', (W, H)); k = min(W / im.width, H / im.height)
    im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
    canvas.alpha_composite(im, ((W - im.width) // 2, (H - im.height) // 2))
    canvas.save(D + path)

for name in ('star-front', 'star-back', 'box-star'):
    old = Image.open(D + name + '.png').size
    cut_grey(name + '-higgsfield-original.png', old).save(D + name + '.png'); print(name, old)
strip_white_border('toy-star-back.png'); print('toy-star-back')

"""Christmas case: the sleigh once the star's box is opened (user request 2026-11-16: the closed box showed under the open
one, and the box should be empty once the star is taken).
- sleigh-nobox.jpg: sleigh.jpg with the front middle box taken away. The Higgsfield edit of the crop (416, 388)-(992, 772)
  (sleigh-nobox-higgsfield-original.png) is scaled back to the crop and only the box's place is pasted, its edge faded.
- box-empty.png: box-empty-higgsfield-original.png (box-star's picture with the star gone, on flat grey) cut out as
  box-star.png was (scripts/cut-christmas-stars.py) and fitted into the same size, so the two lie on the same place.
Run from the project folder."""
from PIL import Image, ImageChops, ImageDraw, ImageFilter

D = 'assets/places/christmas/'
CROP = (416, 388, 992, 772)

def flood_outside(mask):
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

# the sleigh without the middle box
sl = Image.open(D + 'sleigh.jpg').convert('RGB')
w, h = CROP[2] - CROP[0], CROP[3] - CROP[1]
ed = Image.open(D + 'sleigh-nobox-higgsfield-original.png').convert('RGB').resize((w, h), Image.LANCZOS)
# where the box was (in the crop), with a soft edge
mask = Image.new('L', (w, h)); ImageDraw.Draw(mask).rectangle(PATCH := (196, 92, 400, 300), fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(10))
part = sl.crop(CROP); part.paste(ed, (0, 0), mask); sl.paste(part, CROP[:2])
sl.save(D + 'sleigh-nobox.jpg', quality=92)

# the open box, empty
size = Image.open(D + 'box-star.png').size
cut_grey('box-empty-higgsfield-original.png', size).save(D + 'box-empty.png')
print('ok')

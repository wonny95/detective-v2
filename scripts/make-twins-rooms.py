"""The twins' interview pictures (design/case-twins.md, 2026-11-25), both from one Higgsfield picture so that face, body and
room are the same (interview-evan-v2-higgsfield-original.png, job bde5cff8-efe6-4581-b679-f56ced087be5, 2 credits):
- Evan: the picture as drawn, its own gauze and tape (user request 2026-11-25: use the picture as made)
- Milo: without the dressings (the first picture's forehead, which lies exactly under them), the shirt beige, a bandage
  round a finger
- the van on the desk photo as bright as in front of the workshop
Writes interview-evan-v2.png, interview-milo-v2.png (1792 x 2400), interview.webp and evan.webp (the game's).
Run from the project folder: python -I scripts/make-twins-rooms.py"""
import colorsys, random
from PIL import Image, ImageDraw, ImageFilter
D = 'assets/places/twins/'
src = Image.open(D + 'interview-evan-v2-higgsfield-original.png').convert('RGB')
W, H = src.size
first = Image.open(D + 'interview-evan-higgsfield-original.png').convert('RGB').resize((W, H), Image.LANCZOS)
R = random.Random(3)

# the forehead of the first picture (the same drawing), between the ears and down to the eyes
m = Image.new('L', (W, H), 0)
ImageDraw.Draw(m).polygon([(700, 1020), (712, 930), (780, 870), (880, 845), (990, 850), (1070, 900), (1085, 1000), (1060, 1012),
                           (1000, 968), (950, 975), (930, 1000), (876, 1000), (866, 985), (800, 990), (780, 1006), (745, 1030)], fill=255)
base = Image.composite(first, src, m.filter(ImageFilter.GaussianBlur(4)))


def recolor(img, box, pick, to):
    out, mask = img.copy(), Image.new('L', img.size, 0)
    p, o, q = img.load(), out.load(), mask.load()
    for y in range(box[1], box[3]):
        for x in range(box[0], box[2]):
            h, s, v = colorsys.rgb_to_hsv(*(c / 255 for c in p[x, y]))
            w = pick(x, y, h, s, v)
            if w > 0:
                q[x, y] = round(255 * min(1, w))
                o[x, y] = tuple(round(min(1, c) * 255) for c in colorsys.hsv_to_rgb(*to(h, s, v)))
    return Image.composite(out, img, mask.filter(ImageFilter.MedianFilter(3)).filter(ImageFilter.GaussianBlur(1)))


# the van on the photo
photo = lambda img: recolor(img, (1225, 1875, 1600, 2125), lambda x, y, h, s, v: (s - .12) / .16 if .5 < h < .74 else 0,
               lambda h, s, v: (.585, min(1, s * 1.18), min(1, v * 1.32 + .05 * min(1, v * 2))))
base = photo(base)

S = 4
INK = (74, 54, 46, 255)


def sketch(w, h):
    i = Image.new('RGBA', (w * S, h * S), (0, 0, 0, 0))
    return i, ImageDraw.Draw(i)


def bandage(img, a, b, r0, r1):   # round a finger from a to b
    x0, y0, x1, y1 = min(a[0], b[0]) - 60, min(a[1], b[1]) - 60, max(a[0], b[0]) + 60, max(a[1], b[1]) + 60
    i, d = sketch(x1 - x0, y1 - y0)
    at = lambda t: (a[0] + (b[0] - a[0]) * t - x0, a[1] + (b[1] - a[1]) * t - y0, r0 + (r1 - r0) * t)
    for grow, c in ((3.6, INK), (0, (252, 250, 245, 255))):
        for k in range(61):
            x, y, r = at(k / 60); r += grow
            d.ellipse(((x - r) * S, (y - r) * S, (x + r) * S, (y + r) * S), fill=c)
    for t in (.02, .24, .46, .68, .9):   # the turns
        x, y, r = at(t)
        d.line(((x - r * .92) * S, (y + r * .3) * S, (x + r * .92) * S, (y - r * .42) * S), fill=(190, 184, 176, 255), width=int(2.4 * S))
    out = img.convert('RGBA')
    out.alpha_composite(i.resize((x1 - x0, y1 - y0), Image.LANCZOS), (x0, y0))
    return out.convert('RGB')


evan = photo(src)
evan.save(D + 'interview-evan-v2.png')

# the shirt: what its outlines close in (flooded from a point in each part), and only the blue there
x0, y0, x1, y1 = 600, 1180, 1230, 1620
wall = base.crop((x0, y0, x1, y1)).convert('L').point(lambda v: 0 if v < 74 else 255)
for at in ((730, 1400), (810, 1260), (1090, 1400), (1000, 1250), (830, 1330), (960, 1330), (700, 1530), (1120, 1530), (880, 1380), (930, 1400)):
    xy = (at[0] - x0, at[1] - y0)
    if wall.getpixel(xy) == 255:
        ImageDraw.floodfill(wall, xy, 128)
area = Image.new('L', (W, H), 0)
area.paste(wall.point(lambda v: 255 if v == 128 else 0).filter(ImageFilter.MaxFilter(9)), (x0, y0))
ImageDraw.Draw(area).ellipse((912, 1332, 946, 1366), fill=255)   # the button
ap = area.load()
milo = recolor(base, (x0, y0, x1, y1), lambda x, y, h, s, v: 1 if ap[x, y] and .5 < h < .72 and s > .08 else 0,
               lambda h, s, v: (.105, min(.36, .20 + s * .16), min(.95, v * 1.42)))
milo = bandage(milo, (1030, 1726), (1008, 1786), 17, 15)
milo.save(D + 'interview-milo-v2.png')

# the game's picture (1311 x 1200 in the game, half as fine again here): the two rooms with a wall between, cut in to bring
# the twins close: Evan's without its right end, Milo's without its left; and Evan's photo for the review
K = 1.5
px = lambda v: round(v * K)


def bare(img, x0, y0, x1, y1):   # what the cut would leave half of on the desk: the bare desk between the hands, over it
    k = W / 896
    tile = img.crop(tuple(round(v * k) for v in (430, y0, 488, y1)))
    w, h = round((x1 - x0) * k), tile.height
    fill, x, flip = Image.new('RGB', (w, h)), 0, False
    while x < w:
        fill.paste(tile.transpose(Image.FLIP_LEFT_RIGHT) if flip else tile, (x, 0)); x += tile.width; flip = not flip
    soft = Image.new('L', (w, h), 255)
    e = round(2 * k)
    ImageDraw.Draw(soft).rectangle((0, 0, w - 1, h - 1), outline=0, width=e)
    out = img.copy(); out.paste(fill, (round(x0 * k), round(y0 * k)), soft.filter(ImageFilter.GaussianBlur(e / 2)))
    return out


LEFT, WALL, FROM = 650, 30, 265
both = Image.new('RGB', (px(LEFT + WALL + 896 - FROM), px(1200)), (70, 84, 95))
both.paste(bare(evan, 496, 908, 680, 1135).resize((px(896), px(1200)), Image.LANCZOS).crop((0, 0, px(LEFT), px(1200))), (0, 0))
both.paste(bare(bare(milo, 240, 862, 364, 1110), 240, 912, 380, 1110).resize((px(896), px(1200)), Image.LANCZOS).crop((px(FROM), 0, px(896), px(1200))), (px(LEFT + WALL), 0))
d = ImageDraw.Draw(both)
d.line((px(LEFT) + 3, 0, px(LEFT) + 3, px(1200)), fill=(38, 46, 54), width=6)
d.line((px(LEFT + WALL) - 4, 0, px(LEFT + WALL) - 4, px(1200)), fill=(38, 46, 54), width=6)
both.save(D + 'interview.webp', quality=88)
evan.crop((390, 640, 1430, 1600)).resize((780, 720), Image.LANCZOS).save(D + 'evan.webp', quality=88)
print(both.size)

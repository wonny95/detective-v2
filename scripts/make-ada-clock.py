"""Ada's music box made a clock (the twins case, "We fixed a clock.", user pick 2026-11-25, 0 credits): the mantel clock off
the shelf of workshop-higgsfield-original.png, cut out and set on her lap over the box in both pictures; her hand and the
tools come back over it. Writes ada-clock.webp, ada-talk-clock.webp (the sprites, same size, so face and mouths stay).
Run from the project folder: python -I scripts/make-ada-clock.py"""
import random
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter
C = 'assets/characters/'
S = 4
INK = (70, 30, 28, 255)
R = random.Random(5)

# the clock: cut along its outline (coordinates of the shelf's crop, twice its size), with a line of its own round it
shelf = Image.open('assets/places/twins/workshop-higgsfield-original.png').convert('RGB').crop((380, 560, 900, 800)).resize((2080, 960), Image.LANCZOS)
pts = [(501, 360), (501, 306), (520, 299), (545, 290), (566, 270), (575, 240), (580, 205), (596, 172), (622, 143), (656, 123), (694, 117),
       (736, 121), (772, 138), (800, 164), (815, 196), (821, 232), (833, 262), (856, 287), (884, 300), (902, 312), (904, 360)]
m = Image.new('L', shelf.size, 0)
ImageDraw.Draw(m).polygon([(x * 2, y * 2) for x, y in pts], fill=255)
clock = shelf.convert('RGBA'); clock.putalpha(m)
d = ImageDraw.Draw(clock)
d.line([(x * 2, y * 2) for x, y in pts + pts[:2]], fill=INK, width=13, joint='curve')
clock = clock.crop((980, 215, 1830, 732))
rgb = ImageEnhance.Contrast(ImageEnhance.Color(clock.convert('RGB')).enhance(1.25)).enhance(1.08)
clock = Image.merge('RGBA', (*rgb.split(), clock.split()[3]))


def fill_lap(img, poly, edge):   # what the box hid: the apron in pencil strokes, soft into what is there, and its outline
    size = (img.width * S, img.height * S)
    lay = Image.new('RGBA', size, (176, 104, 54, 255))
    q = ImageDraw.Draw(lay)
    for _ in range(900):
        x, y = R.uniform(40, 225), R.uniform(380, 490)
        c = R.choice(((160, 92, 46), (186, 112, 60), (168, 98, 50)))
        q.line((x * S, y * S, (x + R.uniform(5, 14)) * S, (y - R.uniform(2, 7)) * S), fill=(*c, 70), width=int(1.4 * S))
    mask = Image.new('L', size, 0)
    ImageDraw.Draw(mask).polygon([(x * S, y * S) for x, y in poly], fill=255)
    soft = mask.filter(ImageFilter.GaussianBlur(3 * S))   # soft on the right only, where the apron goes on
    hard = Image.new('L', size, 0); hard.paste(mask.crop((0, 0, 190 * S, size[1])), (0, 0))
    soft.paste(hard.crop((0, 0, 186 * S, size[1])), (0, 0))
    lay.putalpha(soft)
    q = ImageDraw.Draw(lay)
    q.line([(x * S, y * S) for x, y in edge], fill=INK, width=int(2.6 * S), joint='curve')
    img.alpha_composite(lay.resize(img.size, Image.LANCZOS))


def erase(img, poly):
    k = Image.new('L', (img.width * S, img.height * S), 0)
    ImageDraw.Draw(k).polygon([(x * S, y * S) for x, y in poly], fill=255)
    k = k.resize(img.size, Image.LANCZOS)
    img.paste(Image.new('RGBA', img.size, (0, 0, 0, 0)), (0, 0), k)


def over(img, src, polys):   # back over the clock, as drawn
    k = Image.new('L', (img.width * S, img.height * S), 0)
    for p in polys:
        ImageDraw.Draw(k).polygon([(x * S, y * S) for x, y in p], fill=255)
    k = k.resize(img.size, Image.LANCZOS)
    img.paste(src, (0, 0), Image.composite(src.split()[3], Image.new('L', img.size, 0), k))


def make(name, out, hands, w=158, at=(130, 486)):
    src = Image.open(C + name).convert('RGBA')
    img = src.copy()
    # the box's left end stands over nothing: off; then the lap and its edge where it was
    erase(img, [(52, 391), (84, 389), (104, 394), (116, 396), (96, 412), (72, 440), (56, 456), (52, 452)])
    erase(img, [(92, 387), (113, 387), (112, 396), (92, 396)])
    fill_lap(img, [(122, 394), (206, 396), (212, 470), (150, 486), (50, 466), (54, 458), (72, 440), (96, 412)],
             [(124, 392), (96, 411), (72, 439), (53, 459)])
    c = clock.resize((w, round(clock.height * w / clock.width)), Image.LANCZOS)
    c = c.rotate(-3, Image.BICUBIC, expand=True)
    # its shadow on the lap
    sh = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).ellipse((at[0] - w * .5, at[1] - 12, at[0] + w * .54, at[1] + 10), fill=(90, 45, 20, 120))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(4)))
    img.alpha_composite(c, (round(at[0] - c.width / 2), at[1] - c.height))
    over(img, src, hands)
    img.save(C + out, quality=92)
    return img


if __name__ == '__main__':
    make('ada-higgsfield.png', 'ada-clock.webp', [
        [(60, 300), (128, 300), (124, 366), (118, 396), (124, 400), (122, 404), (112, 400), (98, 358), (60, 356)],
        [(184, 320), (330, 320), (330, 402), (190, 388), (184, 382), (160, 414), (146, 418), (148, 408), (172, 372)]])
    make('ada-talk-higgsfield.png', 'ada-talk-clock.webp', [
        [(183, 400), (200, 396), (262, 350), (330, 350), (330, 420), (262, 432), (236, 448), (182, 450), (180, 430)]])

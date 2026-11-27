"""Valentine case (design/case-valentine-chocolate.md, "그림 제작 계획" 8): the case list cover and the review photo,
put together from pictures already made (no new art).

- cover.webp (800×563, the list photo's ratio 1.42, as the umbrella cover): classroom v2 with the boxes drawn on the
  desk (classroom-v2-boxes-higgsfield-original.png), cropped around the teacher's desk.
- review-boxes.webp (840×360, the review photo's wide frame): the eight packed gift boxes (gift-closed.webp) in a row
  over the blurred classroom, as at the end of the case.
Run from the project folder: python -I scripts/make-valentine-cover.py   (Pillow only)"""
from PIL import Image, ImageFilter

P = 'assets/places/valentine/'
# classroom v2 (user 2026-11-27): the boxes are drawn on the desk in the picture itself, so the cover is only a crop
room = Image.open(P + 'classroom-v2-higgsfield-original.png').convert('RGBA')
boxed = Image.open(P + 'classroom-v2-boxes-higgsfield-original.png').convert('RGBA')


def shadow(img, blur, alpha, squash=1.0):
    """a dark blurred copy of the picture's shape (squashed downwards for a shadow on a table)"""
    a = img.getchannel('A').point(lambda v: int(v * alpha))
    sh = Image.new('RGBA', img.size, (40, 22, 12, 0)); sh.putalpha(a)
    if squash != 1.0:
        sh = sh.resize((img.width, max(1, round(img.height * squash))))
    pad = blur * 3
    out = Image.new('RGBA', (sh.width + 2 * pad, sh.height + 2 * pad)); out.paste(sh, (pad, pad))
    return out.filter(ImageFilter.GaussianBlur(blur)), pad


# --- cover: the teacher's desk with the boxes, the chalkboard and the paper hearts above it ---
cx = 900                                  # the desk's middle
W = 1040; H = round(W / 1.42)
x0, y0 = cx - W // 2, 650
boxed.crop((x0, y0, x0 + W, y0 + H)).resize((800, round(800 / 1.42)), Image.LANCZOS).convert('RGB') \
    .save(P + 'cover.webp', quality=88, method=6)

# --- review photo: eight packed boxes in a row over the blurred classroom ---
RW, RH = 840, 360
bg = room.crop((300, 760, 1500, 760 + round(1200 * RH / RW))).resize((RW, RH), Image.LANCZOS).filter(ImageFilter.GaussianBlur(6))
dim = Image.new('RGBA', bg.size, (46, 34, 25, 90)); bg.alpha_composite(dim)
g = Image.open(P + 'gift-closed.webp').convert('RGBA')
gs = 92; g = g.resize((gs, round(g.height * gs / g.width)), Image.LANCZOS)
gap = (RW - 8 * gs) // 9
tilts = [-4, 3, -2, 5, -3, 2, -5, 3]
for i, t in enumerate(tilts):
    gi = g.rotate(t, expand=True, resample=Image.BICUBIC)
    gx = gap + i * (gs + gap) - (gi.width - gs) // 2
    gy = (RH - gi.height) // 2 + (8 if i % 2 else -8)
    s, p = shadow(gi, 6, .5)
    bg.alpha_composite(s, (gx - p + 4, gy - p + 6))
    bg.alpha_composite(gi, (gx, gy))
bg.convert('RGB').save(P + 'review-boxes.webp', quality=88, method=6)
print('cover 800x%d, review %dx%d' % (round(800 / 1.42), RW, RH))

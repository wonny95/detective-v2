"""Valentine case (design/case-valentine-chocolate.md, "그림 제작 계획" 8): the case list cover and the review photo,
put together from pictures already made (no new art).

- cover.webp (800×563, the list photo's ratio 1.42, as the umbrella cover): the classroom (classroom-higgsfield-original.png)
  around the teacher's desk, with desk-boxes.webp (the closed chocolate box and small gift boxes, seen as the room is)
  standing on the desk, a soft shadow under it.
- review-boxes.webp (840×360, the review photo's wide frame): the eight packed gift boxes (gift-closed.webp) in a row
  over the blurred classroom, as at the end of the case.
Run from the project folder: python -I scripts/make-valentine-cover.py   (Pillow only)"""
from PIL import Image, ImageFilter

P = 'assets/places/valentine/'
room = Image.open(P + 'classroom-higgsfield-original.png').convert('RGBA')


def shadow(img, blur, alpha, squash=1.0):
    """a dark blurred copy of the picture's shape (squashed downwards for a shadow on a table)"""
    a = img.getchannel('A').point(lambda v: int(v * alpha))
    sh = Image.new('RGBA', img.size, (40, 22, 12, 0)); sh.putalpha(a)
    if squash != 1.0:
        sh = sh.resize((img.width, max(1, round(img.height * squash))))
    pad = blur * 3
    out = Image.new('RGBA', (sh.width + 2 * pad, sh.height + 2 * pad)); out.paste(sh, (pad, pad))
    return out.filter(ImageFilter.GaussianBlur(blur)), pad


# --- cover: the boxes on the teacher's desk (its top runs x 527-1267, y 1191-1293 in the classroom picture) ---
box = Image.open(P + 'desk-boxes.webp').convert('RGBA')
bw = 640; box = box.resize((bw, round(box.height * bw / box.width)), Image.LANCZOS)
cx, base = 905, 1272                      # the desk's middle, the boxes' foot on the desk top
x, y = cx - bw // 2, base - box.height
sh, pad = shadow(box, 10, .45, .25)
cover = room.copy()
cover.alpha_composite(sh, (x - pad + 14, base - sh.height + pad + 6))
cover.alpha_composite(box, (x, y))
W = 1040; H = round(W / 1.42)
x0, y0 = cx - W // 2, 660
cover.crop((x0, y0, x0 + W, y0 + H)).resize((800, round(800 / 1.42)), Image.LANCZOS).convert('RGB') \
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

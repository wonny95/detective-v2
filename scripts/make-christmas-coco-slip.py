"""Coco's hand-over slip seen unfolded (close look 'cocoslip', user request 2026-11-16: folded on her table, open in
the close look, listing whose gifts). The blank paper is Higgsfield's (coco-slip-higgsfield-original.png, magenta
around it); the words are written in here (AI pictures write poorly): her lines in pencil (Ink Free), the four
children ticked, and Nico's name signed in blue ink (Segoe Script).
Run from the project folder: python scripts/make-christmas-coco-slip.py"""
from PIL import Image, ImageDraw, ImageFont
im = Image.open('assets/places/christmas/coco-slip-higgsfield-original.png').convert('RGBA')
W, H = im.size
px = im.load()
# magenta out (soft edge and despill), as the gift list
for y in range(H):
    for x in range(W):
        r, g, b, a = px[x, y]
        mag = min(r, b) - g
        if mag > 90: px[x, y] = (0, 0, 0, 0)
        elif mag > 30:
            k = (mag - 30) / 60
            px[x, y] = (int(r - (r - g) * k * .8), g, int(b - (b - g) * k * .8), int(255 * (1 - k)))
im = im.crop(im.getbbox())
W, H = im.size
d = ImageDraw.Draw(im)
INK, PEN = 'C:/Windows/Fonts/Inkfree.ttf', 'C:/Windows/Fonts/segoesc.ttf'
ink, blue = (63, 51, 38, 255), (47, 79, 134, 255)
f = lambda path, k: ImageFont.truetype(path, int(W * k))
L, R = W * .13, W * .87
y = H * .07
d.text((W / 2, y), 'Hand-over Slip', font=f(INK, .085), fill=ink, anchor='mt')
y += W * .12
d.line([(L, y), (R, y)], fill=ink, width=3)
y += W * .06
d.text((L, y), 'Mittens', font=f(INK, .095), fill=ink)
d.text((R, y + W * .02), 'wrapped by Coco', font=f(INK, .055), fill=ink, anchor='ra')
y += W * .17
step, sz = W * .115, W * .06
for name in ['Ivy', 'Toby', 'Wren', 'Hugo']:
    d.rectangle([L, y + sz * .3, L + sz, y + sz * 1.3], outline=ink, width=3)
    d.line([(L + sz * .15, y + sz * .8), (L + sz * .45, y + sz * 1.15), (L + sz * 1.15, y - sz * .05)], fill=ink, width=5, joint='curve')
    d.text((L + sz * 1.8, y), name, font=f(INK, .085), fill=ink)
    y += step
y += W * .04
d.line([(L, y), (R, y)], fill=ink, width=2)
y += W * .05
d.text((L, y), '4 boxes', font=f(INK, .1), fill=ink)
y += W * .2
d.text((L, y), 'Taken by:', font=f(INK, .07), fill=ink)
d.text((L + W * .33, y - W * .035), 'Nico', font=f(PEN, .12), fill=blue)
im.save('assets/places/christmas/coco-slip.png')
print('coco-slip.png', im.size)

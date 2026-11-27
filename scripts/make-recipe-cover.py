"""Recipe box case: the case list's cover and the review's photo, from the pictures already made (0 credits).

- cover.webp (800x563, as the Valentine cover's 1.42): the kitchen band with the box and the note on the worktable
  (scene-*.webp at their places), cut around the worktable.
- review-card.webp (840x360, as the Valentine review photo): over the blurred kitchen, the recipe card in the middle
  with its title and the lemon cake, the open box behind it.
Run from the project folder: python -I scripts/make-recipe-cover.py   (Pillow only)"""
from PIL import Image, ImageDraw, ImageFilter, ImageFont

P = 'assets/places/recipe/'
band = Image.open(P + 'kitchen.webp').convert('RGBA')
for name, xy in {'scene-box': (1010, 534), 'scene-note': (1094, 672), 'scene-book': (480, 31)}.items():
    band.alpha_composite(Image.open(P + name + '.webp').convert('RGBA'), xy)
# the worktable with the locked box and the note in the middle (the case card shows the middle of the cover), the same
# 1.42 ratio: x 780-1376
w = 596; h = round(w / 1.42)
band.crop((780, 330, 780 + w, 330 + h)).resize((800, round(800 / 1.42)), Image.LANCZOS).convert('RGB').save(P + 'cover.webp', quality=86)

bg = Image.open(P + 'kitchen.webp').convert('RGB').crop((0, 200, 1376, 790)).resize((840, 360), Image.LANCZOS).filter(ImageFilter.GaussianBlur(6))
bg = Image.blend(bg, Image.new('RGB', bg.size, (46, 34, 25)), .3).convert('RGBA')
def put(img, src, w, x, y):
    im = Image.open(src).convert('RGBA'); im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    img.alpha_composite(im, (x, y)); return im.size
# the card in the middle (the review's photo frame shows the middle of the picture), the open box behind it on the left
put(bg, P + 'box-open.webp', 230, 150, 110)
cw, ch = put(bg, P + 'recipe-card.webp', 360, 240, 46)
d = ImageDraw.Draw(bg)
f = ImageFont.truetype('C:/Windows/Fonts/georgiab.ttf', 28)
t = 'Secret Lemon Cake'; tw = d.textlength(t, font=f)
d.text((240 + cw / 2 - tw / 2, 46 + 128), t, font=f, fill=(138, 58, 82))
put(bg, P + 'food/lemon-cake.webp', 140, 240 + cw // 2 - 70, 46 + 170)
bg.convert('RGB').save(P + 'review-card.webp', quality=86)
print('cover.webp', (800, round(800 / 1.42)), 'review-card.webp', bg.size)

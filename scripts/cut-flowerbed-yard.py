"""The flowerbed case's second place, the neighbours' yard where Gus and Pablo play ball (user request 2026-11-23:
the suspects playing ball somewhere else; Pablo plays with a puppy, since tennis alone is odd).
- the yard: one tall 3:4 picture (assets/places/flowerbed/yard-higgsfield-original.png, Nano Banana 2.1 2K, job
  97d6b7b4-3f6a-4837-b26b-7da31d48a96a, the garden as style reference) scaled to 1376 wide; a 1376x768 band from TOP
  is the place (yard.webp: the back fence with the shed and Ollie's flowerbed beyond, the front fence with tulips,
  the doghouse, the lawn), the lawn under it the floor (yard-floor.jpg, mirrored on to FLOOR_H, as the garden).
- playing: one sheet on flat magenta (assets/characters/flowerbed-play-higgsfield-original.png, Nano Banana 2.1 16:9
  2K, job 39110115-6822-4a4f-a790-30cd601c5f0e, Gus's and Pablo's pictures as reference): Gus kicking his soccer ball,
  Pablo throwing his tennis ball, a puppy. Keyed out as scripts/cut-pablo.py, split at the empty columns, 3% margin,
  700 px tall -> gus-play.png/.webp, pablo-play.png/.webp, puppy.png/.webp (assets/characters/).
Run from the project folder: python -I scripts/cut-flowerbed-yard.py"""
from PIL import Image, ImageFilter
P = 'assets/places/flowerbed/'; C = 'assets/characters/'
TOP, FLOOR_H = 360, 900
im = Image.open(P + 'yard-higgsfield-original.png').convert('RGB')
im = im.resize((1376, round(im.height * 1376 / im.width)), Image.LANCZOS)
im.crop((0, TOP, 1376, TOP + 768)).save(P + 'yard.webp', quality=88)
lawn = im.crop((0, TOP + 768, 1376, im.height))
floor = Image.new('RGB', (1376, FLOOR_H)); y, flip = 0, False
while y < FLOOR_H:
    floor.paste(lawn.transpose(Image.FLIP_TOP_BOTTOM) if flip else lawn, (0, y)); y += lawn.height; flip = not flip
floor.save(P + 'yard-floor.jpg', quality=85)
print('yard', im.size, 'lawn h', lawn.height)

src = Image.open(C + 'flowerbed-play-higgsfield-original.png').convert('RGB')
def key_out(img):
    px = img.load(); W0, H0 = img.size
    rgba = img.convert('RGBA'); rp = rgba.load(); alpha = Image.new('L', img.size); ap = alpha.load()
    for y in range(H0):
        for x in range(W0):
            r, g, b = px[x, y]; k = max(0, min(r, b) - g)
            a = 255 if k < 60 else 0 if k > 150 else round(255 * (150 - k) / 90)
            ap[x, y] = a
            if 0 < a < 255 or (a == 255 and k > 25):
                rp[x, y] = (min(r, g + 40) if r > g + 40 else r, g, min(b, g + 40) if b > g + 40 else b, 255)
    rgba.putalpha(alpha.filter(ImageFilter.GaussianBlur(.6)))
    return rgba
for name, (x0, x1) in {'gus-play': (63, 1066), 'pablo-play': (1163, 1990), 'puppy': (2063, 2661)}.items():
    fig = key_out(src.crop((x0, 0, x1, src.height)))
    box = fig.getchannel('A').point(lambda a: 255 if a > 24 else 0).getbbox()
    fig = fig.crop(box); m = round(max(fig.size) * .03)
    out = Image.new('RGBA', (fig.width + 2 * m, fig.height + 2 * m)); out.paste(fig, (m, m))
    s = 700 / out.height; out = out.resize((round(out.width * s), 700), Image.LANCZOS)
    out.save(C + f'{name}.png', optimize=True); out.save(C + f'{name}.webp', quality=90)
    print(name, out.size, 'figure px in sheet', box[3] - box[1])

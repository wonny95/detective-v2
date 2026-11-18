"""Toby Bear, the kite case's client (user decision 2026-11-18: the boy cub, candidate B, instead of Betty):
the Higgsfield picture on white (assets/characters/cub-b-higgsfield-original.png) -> assets/characters/toby-higgsfield.png
(white outside the outline keyed out by a flood fill from the border, soft edge; 3% margin, 700 px tall) and a 160 px
face icon -> assets/ui/icons-v2/toby.png, as scripts/cut-umbrella-characters.py.
Prints the sprite size and the face viewBox for SPRITES. Run from the project folder: python -I scripts/cut-toby.py"""
from PIL import Image, ImageDraw, ImageFilter, ImageChops
D = 'assets/characters/'
src = Image.open(D + 'cub-b-higgsfield-original.png').convert('RGB')
# near-white reached from the border = background (the white inside the eyes stays)
light = src.convert('L').point(lambda v: 255 if v > 232 else 0)
mask = light.copy(); ImageDraw.floodfill(mask, (0, 0), 128)
for p in [(src.width - 1, 0), (0, src.height - 1), (src.width - 1, src.height - 1)]:
    if mask.getpixel(p) == 255: ImageDraw.floodfill(mask, p, 128)
bg = mask.point(lambda v: 255 if v == 128 else 0)
# soft edge: the background grown by 1 px and blurred, the figure is what is left
alpha = ImageChops.invert(bg.filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.GaussianBlur(1.2)))
im = src.convert('RGBA'); im.putalpha(alpha)
box = alpha.point(lambda a: 255 if a > 24 else 0).getbbox()
im = im.crop(box); m = round(max(im.size) * .03)
out = Image.new('RGBA', (im.width + 2 * m, im.height + 2 * m)); out.paste(im, (m, m)); im = out
s = 700 / im.height
im = im.resize((round(im.width * s), 700), Image.LANCZOS)
im.save(D + 'toby-higgsfield.png', optimize=True)
W, H = im.size
cx, y0, side = round(.5 * W), round(.02 * H), round(.5 * H)   # the head with the cap
print('toby', im.size, f"face:'{cx - side // 2} {y0} {side} {side}'")
face = Image.new('RGBA', (side, side)); face.paste(im.crop((cx - side // 2, y0, cx - side // 2 + side, y0 + side)), (0, 0))
icon = Image.new('RGBA', (160, 160)); icon.paste(face.resize((148, 148), Image.LANCZOS), (6, 6))
rim = icon.getchannel('A').point(lambda v: 255 if v > 40 else 0).filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.GaussianBlur(.8))
white = Image.new('RGBA', (160, 160), (255, 255, 255, 255)); white.putalpha(rim)
white.alpha_composite(icon); white.save('assets/ui/icons-v2/toby.png', optimize=True)

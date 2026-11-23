"""Flowerbed case (사건 화단, design/case-flowerbed-ball.md, 2026-11-23): Higgsfield pictures cut for the game.
- the garden: one tall 3:4 picture (assets/places/flowerbed/garden-higgsfield-original.png, Nano Banana 2.1, job
  94c8c605, the kite park as style reference) scaled to 1376 wide; a 1376x768 band from TOP is the place
  (garden.webp: the neighbour's yard with its shed, the fence, the flowerbed with the big round mark, the lawn and
  stepping stones), the lawn under it the floor (garden-floor.jpg, mirrored on to FLOOR_H, as the park).
- Ollie and Gus: one sheet on white (assets/characters/gus-ollie-higgsfield-original.png, job c8f27f30, Toby and the
  picnic sheet as reference), background removed by Higgsfield (gus-ollie-cutout.png, job 03d9fdb3), split at the gap
  between them -> ollie-higgsfield.png / gus-higgsfield.png (3% margin, 700 tall) and Gus's 160 px face icon (Ollie keeps the picnic one).
Prints the sprite sizes and face viewBoxes for SPRITES. Run from the project folder: python -I scripts/cut-flowerbed.py"""
from PIL import Image, ImageFilter
D = 'assets/places/flowerbed/'
TOP, FLOOR_H = 430, 900
im = Image.open(D + 'garden-higgsfield-original.png').convert('RGB')
im = im.resize((1376, round(im.height * 1376 / im.width)), Image.LANCZOS)
im.crop((0, TOP, 1376, TOP + 768)).save(D + 'garden.webp', quality=88)
lawn = im.crop((0, TOP + 768, 1376, im.height))
floor = Image.new('RGB', (1376, FLOOR_H))
y, flip = 0, False
while y < FLOOR_H:
    floor.paste(lawn.transpose(Image.FLIP_TOP_BOTTOM) if flip else lawn, (0, y)); y += lawn.height; flip = not flip
floor.save(D + 'garden-floor.jpg', quality=85)
print('garden', im.size, 'lawn h', lawn.height, 'floor h', FLOOR_H)

C = 'assets/characters/'
sheet = Image.open(C + 'gus-ollie-cutout.png').convert('RGBA')
SPLIT = 1433   # the empty column between them
for name, part, face_top, face_side in [('ollie', sheet.crop((0, 0, SPLIT, sheet.height)), .02, .46), ('gus', sheet.crop((SPLIT, 0, sheet.width, sheet.height)), .02, .44)]:
    a = part.getchannel('A')
    box = a.point(lambda v: 255 if v > 24 else 0).getbbox()
    fig = part.crop(box); m = round(max(fig.size) * .03)
    out = Image.new('RGBA', (fig.width + 2 * m, fig.height + 2 * m)); out.paste(fig, (m, m))
    s = 700 / out.height
    out = out.resize((round(out.width * s), 700), Image.LANCZOS)
    out.save(C + f'{name}-higgsfield.png', optimize=True)
    out.save(C + f'{name}-higgsfield.webp', quality=90)
    W, H = out.size
    # the head: the widest run of the top part (Ollie's tail and Gus's ball sit lower)
    head = out.crop((0, 0, W, round(H * face_side))).getchannel('A').point(lambda v: 255 if v > 40 else 0).getbbox()
    side = round(H * face_side); cx = (head[0] + head[2]) // 2; y0 = round(face_top * H)
    print(name, out.size, f"face:'{cx - side // 2} {y0} {side} {side}'")
    face = Image.new('RGBA', (side, side)); face.paste(out.crop((cx - side // 2, y0, cx - side // 2 + side, y0 + side)), (0, 0))
    icon = Image.new('RGBA', (160, 160)); icon.paste(face.resize((148, 148), Image.LANCZOS), (6, 6))
    rim = icon.getchannel('A').point(lambda v: 255 if v > 40 else 0).filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.GaussianBlur(.8))
    white = Image.new('RGBA', (160, 160), (255, 255, 255, 255)); white.putalpha(rim)
    # Ollie keeps the face icon cut from the picnic sheet (icons-v2/ollie, the same otter); Gus gets his own
    if name == 'gus':
        white.alpha_composite(icon); white.save(f'assets/ui/icons-v2/{name}.png', optimize=True); white.save(f'assets/ui/icons-v2/{name}.webp', quality=90)

# the flower held up (user sketch 2026-11-23: the detective's sleeve and hand hold a flower to the suspect's nose):
# one Higgsfield sheet (flower-hand-higgsfield-original.png, job 714af507, Dalton's poses as reference), background
# removed (flower-hand-cutout.png, job 60fc52ee): the arm with the daisy (left) -> flower-hand.webp (700 wide; prints
# where the daisy's middle is, as shares of the picture, for FLOWERBED_CASE.offers) and the daisy alone (right) ->
# flower.webp (the thing in 소지품)
sheet = Image.open(D + 'flower-hand-cutout.png').convert('RGBA')
# the background removal took the white petals half away (user report 2026-11-23: the daisy looked see-through): every
# hole inside the outline is made solid again (what a flood fill from the border does not reach), soft at its edge
from PIL import ImageDraw, ImageChops
alpha = sheet.getchannel('A')
solid = alpha.point(lambda v: 255 if v > 100 else 0)
outside = solid.copy(); ImageDraw.floodfill(outside, (0, 0), 128)
holes = outside.point(lambda v: 255 if v == 0 else 0).filter(ImageFilter.GaussianBlur(.8))
sheet.putalpha(ImageChops.lighter(alpha, holes))
SPLIT_F = 1800
for name, part, width in [('flower-hand', sheet.crop((0, 0, SPLIT_F, sheet.height)), 700), ('flower', sheet.crop((SPLIT_F, 0, sheet.width, sheet.height)), 420)]:
    box = part.getchannel('A').point(lambda v: 255 if v > 24 else 0).getbbox()
    fig = part.crop(box)
    s = width / fig.width
    out = fig.resize((width, round(fig.height * s)), Image.LANCZOS)
    out.save(D + f'{name}.webp', quality=90)
    print(name, out.size, 'box', box)
    if name == 'flower-hand':
        # the daisy's yellow middle in the original sheet (about 510, 360), as shares of the cut picture
        cx, cy = (510 - box[0]) * s / out.width, (360 - box[1]) * s / out.height
        print(f"  daisy middle at [{cx:.3f}, {cy:.3f}], height/width {out.height / out.width:.3f}")

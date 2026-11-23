"""RETIRED 2026-11-23 (user: the white eyes looked scary): no longer run; all poses have dot eyes now, see
scripts/make-dalton-doteyes.py. Kept for the record.

Dalton's eyes made alike (user request 2026-11-23: the default pose and the wave had plain dot eyes while the lens,
point and thinking poses have white eyes with a pupil): the two dot-eyed sprites get white eyes drawn over the dots,
sized as the point pose's (about 40 x 37 px at 700 tall, a dark outline), the pupil big and looking straight ahead, no
highlight (as the drawn ones). Credit-free, drawn here at 4x and scaled down. Then Dalton's face icon is cut again from the default pose.
Run after scripts/cut-dalton-terry.py (it writes the dot-eyed sprites): python -I scripts/fix-dalton-eyes.py
Writes assets/characters/dalton.png/.webp, dalton-wave.png/.webp, assets/ui/icons-v2/dalton.png/.webp."""
from PIL import Image, ImageDraw, ImageFilter
import random
D = 'assets/characters/'
# the dot eyes' centres (sprite px, measured on the 700-tall sprites)
EYES = { 'dalton':[(200, 207), (312.5, 206.5)], 'dalton-wave':[(169, 201.5), (269, 201)] }
W, H, K = 42, 39, 4          # the whole eye, its outline included; drawn K times larger
INK, WHITE, PUPIL = (62, 32, 26, 255), (252, 248, 238, 255), (48, 24, 21, 255)

def eye(seed):
    rnd = random.Random(seed)
    im = Image.new('RGBA', (W * K, H * K)); d = ImageDraw.Draw(im)
    d.ellipse((0, 0, W * K - 1, H * K - 1), fill=INK)
    o = round(3.3 * K); d.ellipse((o, o, W * K - 1 - o, H * K - 1 - o), fill=WHITE)
    pw, ph = 23 * K, 28 * K; cx, cy = W * K / 2, H * K / 2 + 1 * K
    d.ellipse((cx - pw / 2, cy - ph / 2, cx + pw / 2, cy + ph / 2), fill=PUPIL)
    # a little crayon grain on the white, as the drawn eyes
    px = im.load()
    for _ in range(W * H * 3):
        x, y = rnd.randrange(W * K), rnd.randrange(H * K)
        if px[x, y] == WHITE: px[x, y] = (236, 230, 218, 255)
    return im.resize((W, H), Image.LANCZOS)

for name, eyes in EYES.items():
    im = Image.open(D + f'{name}.png').convert('RGBA')
    for i, (x, y) in enumerate(eyes):
        e = eye(i)
        im.alpha_composite(e, (round(x - W / 2), round(y - H / 2)))
    im.save(D + f'{name}.png', optimize=True); im.save(D + f'{name}.webp', quality=90)
    print(name, 'eyes drawn')

# the face icon again from the default pose (as cut-dalton-terry.py: head (.5, 0, .56))
im = Image.open(D + 'dalton.png').convert('RGBA'); Wd, Hd = im.size
cx, y0, side = round(.5 * Wd), 0, round(.56 * Hd)
face = Image.new('RGBA', (side, side)); face.paste(im.crop((cx - side // 2, y0, cx + side - side // 2, y0 + side)), (0, 0))
ic = Image.new('RGBA', (160, 160)); ic.paste(face.resize((148, 148), Image.LANCZOS), (6, 6))
rim = ic.getchannel('A').point(lambda v: 255 if v > 40 else 0).filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.GaussianBlur(.8))
white = Image.new('RGBA', (160, 160), (255, 255, 255, 255)); white.putalpha(rim)
white.alpha_composite(ic); white.save('assets/ui/icons-v2/dalton.png', optimize=True); white.save('assets/ui/icons-v2/dalton.webp', quality=90)
print('icon dalton')

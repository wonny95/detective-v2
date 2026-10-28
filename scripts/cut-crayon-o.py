"""Cut assets/ui/crayon-o-higgsfield-original.png (one red crayon loop on white, started at the bottom left and run
counter-clockwise, its end overlapping inside the start at the bottom) into two transparent layers of the same size:
crayon-o-1.png, the whole loop but the overlapping end, and crayon-o-2.png, that end. The game uncovers each with a
conic mask around the loop's centre (CENTRE below, printed in % of the cut)."""
import math
from PIL import Image

SRC = 'assets/ui/crayon-o-higgsfield-original.png'
INK = (164, 53, 44)                 # #A4352C, the board's red
CENTRE = (452, 600)                 # the loop's middle in the original
AXES = (305, 455)                   # its half width and half height, roughly
# the end: the inner of the two strokes at the bottom, right of x 265 and above this line between them (traced)
SPLIT = [(265, 1048), (350, 1042), (400, 1036), (450, 1020), (500, 996), (550, 964), (590, 930), (600, 918)]
W = 200

def split(x):
    for (x1, y1), (x2, y2) in zip(SPLIT, SPLIT[1:]):
        if x1 <= x <= x2:
            return y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    return 0

src = Image.open(SRC).convert('RGB')
w, h = src.size
px = src.load()
layers = [Image.new('RGBA', (w, h)) for _ in range(2)]
lp = [l.load() for l in layers]
for y in range(h):
    for x in range(w):
        r, g, b = px[x, y]
        a = max(0, min(255, round((255 - (g + b) / 2) / (255 - 60) * 255)))
        if a < 12:
            continue
        k = a / 255
        c = tuple(max(0, min(255, round((v - (1 - k) * 255) / k))) for v in (r, g, b)) if k > .2 else INK
        dx, dy = x - CENTRE[0], y - CENTRE[1]
        rad = math.hypot(dx / AXES[0], dy / AXES[1])
        if not .7 < rad < 1.3:      # specks off the loop (and the faint image edge)
            continue
        end = 265 <= x <= 600 and y > 880 and y < split(x)
        lp[1 if end else 0][x, y] = (*c, a)

boxes = [l.getbbox() for l in layers]
box = (min(b[0] for b in boxes) - 8, min(b[1] for b in boxes) - 8, max(b[2] for b in boxes) + 8, max(b[3] for b in boxes) + 8)
H = round(W * (box[3] - box[1]) / (box[2] - box[0]))
for n, l in enumerate(layers, 1):
    l.crop(box).resize((W, H), Image.LANCZOS).save(f'assets/ui/crayon-o-{n}.png', optimize=True)
print('box', box, 'size', (W, H), 'centre %', round((CENTRE[0] - box[0]) / (box[2] - box[0]) * 100, 1),
      round((CENTRE[1] - box[1]) / (box[3] - box[1]) * 100, 1))

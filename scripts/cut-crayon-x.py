"""Cut assets/ui/crayon-x-higgsfield-original.png (a red crayon X on white) into two transparent strokes:
crayon-x-1.png (top-left to bottom-right, drawn first) and crayon-x-2.png (top-right to bottom-left).
Alpha comes from how far a pixel is from white; each pixel goes to the stroke whose centre line is nearer,
except that the first stroke keeps its whole band (the crossing), so it is whole once drawn."""
from PIL import Image

SRC = 'assets/ui/crayon-x-higgsfield-original.png'
INK = (164, 53, 44)          # #A4352C, the board's red
# the strokes' centre lines in the original (eyeballed ends)
A = ((165, 140), (880, 900))
B = ((875, 95), (140, 880))
SIZE = 240
HALF = 64                    # the first stroke keeps its whole width, the crossing included

def dist(p, line):
    (x1, y1), (x2, y2) = line
    dx, dy = x2 - x1, y2 - y1
    return abs(dy * (p[0] - x1) - dx * (p[1] - y1)) / (dx * dx + dy * dy) ** .5

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
        # the colour without the white mixed in, so the light grainy edges stay red on cream paper
        k = a / 255
        c = tuple(max(0, min(255, round((v - (1 - k) * 255) / k))) for v in (r, g, b)) if k > .2 else INK
        lp[0 if dist((x, y), A) <= HALF or dist((x, y), A) <= dist((x, y), B) else 1][x, y] = (*c, a)

box = layers[0].getbbox()
b2 = layers[1].getbbox()
box = (min(box[0], b2[0]), min(box[1], b2[1]), max(box[2], b2[2]), max(box[3], b2[3]))
side = max(box[2] - box[0], box[3] - box[1]) + 16
cx, cy = (box[0] + box[2]) // 2, (box[1] + box[3]) // 2
sq = (cx - side // 2, cy - side // 2, cx + side // 2, cy + side // 2)
for n, l in enumerate(layers, 1):
    l.crop(sq).resize((SIZE, SIZE), Image.LANCZOS).save(f'assets/ui/crayon-x-{n}.png', optimize=True)
print('crop', sq)

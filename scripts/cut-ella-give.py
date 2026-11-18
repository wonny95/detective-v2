"""Ella holding the umbrella out on both hands (umbrella case v2, user request 2026-11-18): the Higgsfield picture on flat
magenta (assets/characters/ella-give-higgsfield-original.png, job 56109bd9) -> assets/characters/ella-give.png, the
magenta keyed out (with despill), cut to the figure + 3% margin, height 700 like ella-higgsfield.png.
Prints where the umbrella sits in the sprite (px) for the tap spot in index.html.

Run: python -I scripts/cut-ella-give.py   (Pillow only)
"""
import os
from PIL import Image
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'characters') + '/'
src = Image.open(D + 'ella-give-higgsfield-original.png').convert('RGB')
W, H = src.size
px = src.load()
out = Image.new('RGBA', src.size)
op = out.load()
for y in range(H):
    for x in range(W):
        r, g, b = px[x, y]
        # magenta: red and blue high, green low; how far from it decides the alpha
        mag = min(r, b) - g
        a = 255 if mag < 60 else max(0, 255 - int((mag - 60) * 255 / 70))
        if a < 255 and mag > 0:   # despill: pull the pink fringe back toward neutral
            k = min(r, b) - (g + 25)
            if k > 0: r, b = r - k, b - k
        op[x, y] = (r, g, b, a)
bb = out.getchannel('A').point(lambda v: 255 if v > 40 else 0).getbbox()
m = int((bb[3] - bb[1]) * .03)
bb = (max(bb[0] - m, 0), max(bb[1] - m, 0), min(bb[2] + m, W), min(bb[3] + m, H))
fig = out.crop(bb)
s = 700 / fig.size[1]
fig = fig.resize((round(fig.size[0] * s), 700), Image.LANCZOS)
# the body in the middle of the picture (the umbrella reaches further to the left), so the deer stands where the
# plain sprite stands: pad the shorter side, centred on the head
A = fig.getchannel('A')
head = A.crop((0, 0, fig.size[0], 300)).point(lambda v: 255 if v > 128 else 0).getbbox()
cx = (head[0] + head[2]) / 2
half = max(cx, fig.size[0] - cx)
pad = Image.new('RGBA', (round(half * 2), 700), (0, 0, 0, 0))
pad.alpha_composite(fig, (round(half - cx), 0))
fig = pad
fig.save(D + 'ella-give.png', optimize=True)
print('ella-give.png', fig.size)
# the umbrella: its tip (thin and grey) and handle are the figure's leftmost and rightmost pixels in the band of the
# arms; the box in index.html (hold.box) is this with a few px around
A = fig.getchannel('A')
xs = [x for y in range(400, 445) for x in range(fig.size[0]) if A.getpixel((x, y)) > 128]
print('umbrella left/right (sprite px)', min(xs), max(xs), 'rows about 356..495')

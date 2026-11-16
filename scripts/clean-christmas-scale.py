"""The Christmas scale without its white sticker border (user report 2026-11-16: the cut-out looked wrong). The background
removal of the item sheet left a white halo round the scale and filled the gaps between its strings with blurred white.
Everything near-white that is joined to the transparent outside (through other near-white pixels) is taken out; the
light pixels left along the drawn outline fade out by how white they are, so no pale fringe stays. The scale's own
greys and gold are darker than the halo (their darkest channel is under 210), so they stay.
Source: scale-sticker-original.png (the cut-out as it was). Run from the project folder:
python scripts/clean-christmas-scale.py"""
from collections import deque
from PIL import Image

SRC, OUT = 'assets/places/christmas/scale-sticker-original.png', 'assets/places/christmas/scale.png'
im = Image.open(SRC).convert('RGBA')
W, H = im.size
px = im.load()
WHITE = 226   # near-white: every channel at least this


def whiteish(x, y):
    r, g, b, a = px[x, y]
    # the border's outer edge is cream (red at least 236, darkest channel ~200): the scale's greys never get that warm
    return a < 128 or min(r, g, b) >= WHITE or (r >= 236 and min(r, g, b) >= 185)


# flood the outside: from every border pixel and every see-through pixel, through near-white ones
out = bytearray(W * H)
q = deque()
for y in range(H):
    for x in range(W):
        if px[x, y][3] < 128 or x in (0, W - 1) or y in (0, H - 1):
            if whiteish(x, y):
                out[y * W + x] = 1
                q.append((x, y))
while q:
    x, y = q.popleft()
    for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if 0 <= nx < W and 0 <= ny < H and not out[ny * W + nx] and whiteish(nx, ny):
            out[ny * W + nx] = 1
            q.append((nx, ny))

res = im.copy()
rp = res.load()
for y in range(H):
    for x in range(W):
        if out[y * W + x]:
            rp[x, y] = (0, 0, 0, 0)
# the edge left next to what was taken out: light pixels fade by their whiteness (190 → kept, WHITE → gone)
for y in range(H):
    for x in range(W):
        if out[y * W + x]:
            continue
        if not any(0 <= nx < W and 0 <= ny < H and out[ny * W + nx] for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1))):
            continue
        r, g, b, a = rp[x, y]
        m = min(r, g, b)
        if m > 190:
            rp[x, y] = (r, g, b, round(a * max(0, (WHITE - m)) / (WHITE - 190)))
res.save(OUT)
print('saved', OUT, res.size)

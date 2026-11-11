"""Remove the white sticker outline around a cut-out character (the Holly/May/Nico sheet was drawn as stickers).

usage: python scripts/remove-sticker-border.py <in.png> <out.png> [lightest-dark]
  lightest-dark (default 150): pixels whose darkest channel is above it count as rim; Holly's outline-less wool
  needs 200, then [rings] (default 0) more rings of the greyer rim.
  From the transparent outside, floods through light, unsaturated pixels (the white rim and its soft edge) and makes
  them transparent, trims and scales to 700 px high; it stops at the dark drawn outline, so white inside the figure (wool, belly, paper) stays.
"""
import sys
from collections import deque
from PIL import Image

src, dst = sys.argv[1], sys.argv[2]
limit = int(sys.argv[3]) if len(sys.argv) > 3 else 150
im = Image.open(src).convert('RGBA'); px = im.load(); w, h = im.size

def rim(p):
    r, g, b, a = p
    if a < 40: return True
    return min(r, g, b) > limit and max(r, g, b) - min(r, g, b) < 45

seen = bytearray(w * h); q = deque()
for x in range(w):
    for y in (0, h - 1): q.append((x, y))
for y in range(h):
    for x in (0, w - 1): q.append((x, y))
while q:
    x, y = q.popleft()
    if x < 0 or y < 0 or x >= w or y >= h or seen[y * w + x]: continue
    seen[y * w + x] = 1
    if not rim(px[x, y]): continue
    px[x, y] = (0, 0, 0, 0)
    q.extend(((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))
# then a few rings of the greyer rim only, for a figure flooded with the higher limit (Holly)
for _ in range(int(sys.argv[4]) if len(sys.argv) > 4 else 0):
    clear = [(x, y) for y in range(1, h - 1) for x in range(1, w - 1)
             if px[x, y][3] and min(px[x, y][:3]) > 150 and max(px[x, y][:3]) - min(px[x, y][:3]) < 45
             and any(px[x + dx, y + dy][3] == 0 for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))]
    for x, y in clear: px[x, y] = (0, 0, 0, 0)
# soften the new edge: pixels next to the cleared area that are still light grey become half see-through
for y in range(1, h - 1):
    for x in range(1, w - 1):
        r, g, b, a = px[x, y]
        if a and min(r, g, b) > 170 and any(px[x + dx, y + dy][3] == 0 for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
            px[x, y] = (r, g, b, a // 2)
bbox = im.getbbox(); im = im.crop(bbox)
# back to the sprites' 700 px height; print where the old picture's pixels moved (to move face boxes)
k = 700 / im.size[1]
im = im.resize((round(im.size[0] * k), 700), Image.LANCZOS)
im.save(dst); print(dst, im.size, 'offset', bbox[:2], 'scale', round(k, 4))

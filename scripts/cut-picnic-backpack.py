"""The picnic table's blue backpack (picnic-wide.png) cut out with no credits, for the garden bench: the drawing's dark
outline closes the bag, so everything reachable from the crop's edge without crossing it is background; the green
showing through the handle loop is cleared too. -> assets/places/picnic-storyboard/backpack-blue.png and
backpack-red.png (the same bag with its blue turned red, Ollie's). The crop and the traced silhouette reach below the
bag's bottom outline (y 424), or the bag is cut flat (user report)."""
import colorsys
from collections import deque
from PIL import Image, ImageDraw, ImageFilter
SRC, BOX = 'assets/places/picnic-storyboard/picnic-wide.png', (975, 310, 1100, 430)
im = Image.open(SRC).convert('RGB').crop(BOX)
W, H = im.size; px = im.load()
hsv = [[colorsys.rgb_to_hsv(*(c / 255 for c in px[x, y])) for x in range(W)] for y in range(H)]
dark = Image.new('L', (W, H)); dp = dark.load()
for y in range(H):
    for x in range(W):
        dp[x, y] = 255 if hsv[y][x][2] < .45 else 0
dark = dark.filter(ImageFilter.MaxFilter(3)); dp = dark.load()   # seal one-pixel gaps in the outline
bg = [[False] * W for _ in range(H)]
q = deque((x, y) for x in range(W) for y in (0, H - 1)); q.extend((x, y) for y in range(H) for x in (0, W - 1))
while q:
    x, y = q.popleft()
    if not (0 <= x < W and 0 <= y < H) or bg[y][x] or dp[x, y]: continue
    bg[y][x] = True; q.extend(((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))
# the bag's rough silhouette, traced by hand: the trunk and table lines touching its outline stay outside
outline = Image.new('L', (W, H)); ImageDraw.Draw(outline).polygon([(p[0] / 4, p[1] / 4) for p in
    [(200, 38), (300, 38), (302, 96), (348, 104), (384, 170), (424, 262), (462, 330), (468, 400), (456, 420), (400, 440),
     (372, 458), (100, 458), (76, 444), (44, 410), (40, 330), (66, 200), (88, 110), (150, 94), (202, 84)]], fill=255)
op = outline.load()
alpha = Image.new('L', (W, H)); ap = alpha.load()
for y in range(H):
    for x in range(W):
        h, s, v = hsv[y][x]
        green = 60 / 360 <= h <= 170 / 360 and s > .2 and v > .3
        # the table showing through the shoulder strap's loop (bright orange; the strap itself is a darker brown)
        table = 95 <= x <= 112 and 83 <= y <= 103 and 15 / 360 <= h <= 45 / 360 and v > .7
        ap[x, y] = 0 if bg[y][x] or green or table or not op[x, y] else 255
# only the bag itself: the largest piece (stray bits of trunk or table edge enclosed by other lines go)
seen = [[False] * W for _ in range(H)]; best = []
for sy in range(H):
    for sx in range(W):
        if seen[sy][sx] or not ap[sx, sy]: continue
        part, q = [], deque([(sx, sy)]); seen[sy][sx] = True
        while q:
            x, y = q.popleft(); part.append((x, y))
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= nx < W and 0 <= ny < H and not seen[ny][nx] and ap[nx, ny]: seen[ny][nx] = True; q.append((nx, ny))
        if len(part) > len(best): best = part
alpha = Image.new('L', (W, H)); ap = alpha.load()
for x, y in best: ap[x, y] = 255
# soften the edge a little
alpha = alpha.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.GaussianBlur(.6))
blue = im.convert('RGBA'); blue.putalpha(alpha)
blue = blue.crop(alpha.point(lambda a: 255 if a > 40 else 0).getbbox())
# the cloth is a warm grey in the evening light: tinted clearly blue (Mia's) or red (Ollie's); the brown straps and the
# dark outline stay
def tint(img, hue, sat):
    out = img.copy(); op_ = out.load()
    for y in range(out.height):
        for x in range(out.width):
            r, g, b, a = op_[x, y]
            h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
            strap = 15 / 360 <= h <= 45 / 360 and s > .25
            if a and v > .3 and s < .3 and not strap:
                op_[x, y] = (*(round(c * 255) for c in colorsys.hsv_to_rgb(hue / 360, sat + s, v)), a)
    return out
tint(blue, 208, .3).save('assets/places/picnic-storyboard/backpack-blue.png')
tint(blue, 3, .5).save('assets/places/picnic-storyboard/backpack-red.png')
print(blue.size)

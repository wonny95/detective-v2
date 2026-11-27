"""Recipe box case (design/case-recipe-box.md, "그림·녹음"): cut the props out of the magenta prop sheet.

- props-sheet-higgsfield-original.png  job d033c844-4513-49b8-9faf-801c8ce85eab (Nano Banana 2.1 16:9 2K, references: the
  kitchen job 9b399ebd and the spelling padlock job 3854cbc4 for the style)
The magenta is keyed out (soft edge), each object is found as a large non-magenta blob and saved by its place on the sheet.
Run from the project folder: python -I scripts/cut-recipe-props.py   (Pillow only)"""
from PIL import Image, ImageFilter

P = 'assets/places/recipe/'
im = Image.open(P + 'props-sheet-higgsfield-original.png').convert('RGB')
W, H = im.size
px = im.load()

def magenta(r, g, b):
    return r > 150 and b > 150 and g < 120 and abs(r - b) < 90

# alpha: 0 on magenta, 255 elsewhere, softened a little; magenta fringe pulled toward the neighbour colour
alpha = Image.new('L', (W, H))
ap = alpha.load()
for y in range(H):
    for x in range(W):
        r, g, b = px[x, y]
        ap[x, y] = 0 if magenta(r, g, b) else 255
alpha = alpha.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1))
rgba = im.convert('RGBA'); rgba.putalpha(alpha)
# remove the pink cast left on edge pixels: where alpha is partial, lower red/blue toward green
data = rgba.load()
for y in range(H):
    for x in range(W):
        r, g, b, a = data[x, y]
        if 0 < a < 255 and r > g + 60 and b > g + 60:
            m = (r + g + b) // 3
            data[x, y] = (m, m, m, a // 2)

# boxes of the objects (in the 2752×1536 sheet), found by eye from the sheet and padded; the script trims to the alpha
# only the close-up props: the closed box, the note on the table and the book on the shelf did not match the kitchen's
# angle (user 2026-11-27) and are drawn into the kitchen instead (scripts/cut-recipe-places.py, scene-*.webp)
BOXES = {
    'box-open':     (1030, 50, 1800, 720),
    'recipe-card':  (100, 890, 760, 1400),
    'book-open':    (1320, 780, 2200, 1420),
    'note':         (2230, 840, 2690, 1400),
}
for name, (x0, y0, x1, y1) in BOXES.items():
    part = rgba.crop((x0, y0, x1, y1))
    bb = part.getchannel('A').point(lambda v: 255 if v > 40 else 0).getbbox()
    part = part.crop(bb)
    part.save(P + name + '.webp', quality=90, method=6)
    print(name, part.size, 'from', (x0 + bb[0], y0 + bb[1]))

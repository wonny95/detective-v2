"""Cut the note's index tabs from a Higgsfield sheet (six tabs 3x2 on magenta, drawn with the notebook paper's grainy pencil
line; the paper reference was cut from casefile-cutout-original.png). The grainy line lets the magenta through between
its grains, so the tab's shape is the drawing with its gaps closed and filled, and the magenta inside it is painted with
the line's brown. The line is thickened a little (it is drawn at 58px on screen, about as heavy as the page's edge) and
redrawn as one ink on white, so the tab multiplied over a colour shows exactly that colour (the open tab = the page's
cream); the bottom outline is cut off (the tab comes out from under the page), the width 160px.
  python scripts/cut-note-tabs.py assets/ui/tabs-pencil-a-higgsfield-original.png assets/ui/tab   (user pick A)
  -> <prefix>-1.png … -3.png (the top row); a third argument sets how much the line is thickened (default 5px)"""
import sys
from PIL import Image, ImageChops, ImageDraw, ImageFilter

LINE = (52, 44, 42)   # the page's pencil line (casefile-panel.webp)

src, prefix = sys.argv[1], sys.argv[2]
grow = int(sys.argv[3]) if len(sys.argv) > 3 else 5
sheet = Image.open(src).convert('RGB')
W, H = sheet.size
r_, g_, b_ = sheet.split()
magenta = ImageChops.subtract(ImageChops.darker(r_, b_), g_)          # 255 on pure magenta, 0 on the drawing
for n in range(3):
    box = (n * W // 3, 0, (n + 1) * W // 3, H // 2)
    cell, mg = sheet.crop(box), magenta.crop(box)
    ink = mg.point(lambda v: 255 if v < 90 else 0)
    shape = ink.filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.MinFilter(7))
    outside = shape.copy(); ImageDraw.floodfill(outside, (0, 0), 128)
    shape = outside.point(lambda v: 0 if v == 128 else 255)          # holes filled
    l, t, r, b = shape.getbbox()
    cell, shape, ink = cell.crop((l, t, r, b)), shape.crop((l, t, r, b)), ink.crop((l, t, r, b))
    w, h = cell.size
    px, sp, ip = cell.load(), shape.load(), ink.load()
    mid = [px[x, y] for x in range(w // 4, 3 * w // 4, 3) for y in range(h // 4, 3 * h // 4, 3)]
    paper = [sorted(c[i] for c in mid)[len(mid) // 2] for i in range(3)]
    dark = [p for p in (px[x, y] for x in range(w) for y in range(h) if ip[x, y]) if sum(p) < 300]
    line = [sorted(c[i] for c in dark)[len(dark) // 2] for i in range(3)]
    for y in range(h):
        for x in range(w):
            if sp[x, y] and not ip[x, y]: px[x, y] = tuple(line)       # magenta between the grains -> the line's brown
    if grow: cell = cell.filter(ImageFilter.MinFilter(grow))           # the line a little heavier, inward
    # the bottom outline: from the bottom up to the paper, the highest it reaches across the middle 80%
    px = cell.load()
    light = lambda x, y: sum(px[x, y]) > 600
    cut = min(next(y for y in range(h - 1, 0, -1) if light(x, y)) for x in range(w // 10, w - w // 10))
    cell = cell.point(lambda v: v).crop((0, 0, w, cut - 1)); shape = shape.crop((0, 0, w, cut - 1))
    # one ink: how dark a pixel is (by its green, which the magenta does not touch) mixes white toward the page's line colour
    g = cell.getchannel('G')
    d = g.point(lambda v: max(0, min(255, round((paper[1] - v) * 255 / (paper[1] - 45)))))
    cell = Image.merge('RGB', [d.point(lambda v, c=c: round(255 - v * (255 - c) / 255)) for c in LINE])
    tab = cell.convert('RGBA'); tab.putalpha(shape.filter(ImageFilter.GaussianBlur(.7)))
    tab = tab.convert('RGBa').resize((160, round(tab.height * 160 / w)), Image.LANCZOS).convert('RGBA')
    tab.save(f'{prefix}-{n + 1}.png', optimize=True)
    print(f'{prefix}-{n + 1}.png', tab.size, 'paper', paper, 'line', line)

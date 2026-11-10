"""Cut the Christmas star case's Higgsfield pictures for the game (Pillow only).

usage: python scripts/cut-christmas-assets.py <folder with the downloads>
  the folder holds people-nobg.png (Holly·May·Nico sheet, background removed), nico-nervous-nobg.png,
  items-nobg.png (item sheet, background removed), tree-lit.png, map.png
and the repo has assets/places/christmas/{tree,storeroom,tent-fixed,sleigh,corner}-*-original.jpg.

Places: one tall picture each (1792x2400, as the umbrella and violin cases) scaled to 1376x1843; a 768 band from
`top` is the place picture, the rest its floor. People: each figure cut out of the sheet by its columns of
opaque pixels, trimmed with a 3% margin and scaled to 700 px high. Items: each object cut out by its cell.
"""
import sys
from PIL import Image

SRC = sys.argv[1]
PL = 'assets/places/christmas/'
CH = 'assets/characters/'

def band(src, name, top, out_floor=True):
    im = Image.open(src).convert('RGB').resize((1376, 1843), Image.LANCZOS)
    im.crop((0, top, 1376, top + 768)).save(f'{PL}{name}.jpg', quality=88)
    if out_floor:
        im.crop((0, top + 768, 1376, 1843)).save(f'{PL}{name}-floor.jpg', quality=85)
    return 1843 - top - 768

def opaque_runs(im, axis, gap):
    """runs of columns (axis 0) or rows (axis 1) that hold opaque pixels, split where `gap` empty lines come"""
    a = im.getchannel('A').point(lambda v: 255 if v > 40 else 0)
    w, h = a.size
    if axis == 0:
        filled = [a.crop((x, 0, x + 1, h)).getbbox() is not None for x in range(w)]
    else:
        filled = [a.crop((0, y, w, y + 1)).getbbox() is not None for y in range(h)]
    runs, start, empty = [], None, 0
    for i, f in enumerate(filled):
        if f:
            if start is None: start = i
            empty = 0
        elif start is not None:
            empty += 1
            if empty >= gap:
                runs.append((start, i - empty + 1)); start = None; empty = 0
    if start is not None: runs.append((start, len(filled)))
    return runs

def trim(im, margin=.03, height=None):
    box = im.getchannel('A').point(lambda v: 255 if v > 40 else 0).getbbox()
    im = im.crop(box)
    m = int(max(im.size) * margin)
    out = Image.new('RGBA', (im.width + 2 * m, im.height + 2 * m), (0, 0, 0, 0)); out.paste(im, (m, m))
    if height:
        out = out.resize((round(out.width * height / out.height), height), Image.LANCZOS)
    return out

if __name__ == '__main__':
    floors = {}
    for name, src, top in [('tree', f'{PL}tree-higgsfield-original.jpg', 330), ('storeroom', f'{PL}storeroom-higgsfield-original.jpg', 380),
                           ('tent', f'{PL}tent-fixed-original.jpg', 520), ('sleigh', f'{PL}sleigh-higgsfield-original.jpg', 260),
                           ('tree-lit', f'{SRC}/tree-lit.png', 330)]:
        floors[name] = band(src, name, top, name != 'tree-lit')
    print('floors', floors)
    # the storeroom corner photo (c-track-yard) and the map as they are
    Image.open(f'{PL}corner-higgsfield-original.jpg').convert('RGB').save(f'{PL}corner.jpg', quality=88)
    Image.open(f'{SRC}/map.png').convert('RGB').save(f'{PL}map-festival.webp', quality=86)
    # people
    sheet = Image.open(f'{SRC}/people-nobg.png').convert('RGBA')
    runs = opaque_runs(sheet, 0, 20)
    print('people runs', runs)
    for (x0, x1), pid in zip(runs, ['holly', 'mae', 'nico']):
        fig = trim(sheet.crop((x0, 0, x1, sheet.height)), height=700)
        fig.save(f'{CH}{pid}-higgsfield.png'); print(pid, fig.size)
    nv = trim(Image.open(f'{SRC}/nico-nervous-nobg.png').convert('RGBA'), height=700)
    nv.save(f'{CH}nico-nervous-higgsfield.png'); print('nico-nervous', nv.size)
    # items: two rows of three
    it = Image.open(f'{SRC}/items-nobg.png').convert('RGBA')
    rows = opaque_runs(it, 1, 12)
    print('item rows', rows)
    names = [['toy-star-back', 'box-star', 'star-back'], ['box-mittens', 'box-closed', 'scale']]
    for (y0, y1), row in zip(rows, names):
        strip = it.crop((0, y0, it.width, y1))
        cols = opaque_runs(strip, 0, 15)
        print(' cols', cols)
        for (x0, x1), n in zip(cols, row):
            piece = trim(strip.crop((x0, 0, x1, strip.height)), margin=.02)
            piece.save(f'{PL}{n}.png'); print(n, piece.size)

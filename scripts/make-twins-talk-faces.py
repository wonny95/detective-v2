"""The twin case's talking faces (user: when they talk they look at the player).

usage: python scripts/make-twins-talk-faces.py   (after scripts/cut-twins-characters.py)
  Evan's and Milo's sprites look up; three faces (evan, milo, ada-talk, 240 px squares as in FACES) were put on one
  sheet (mouths/twins-faces2-before.png) and edited once on Higgsfield (mouths/twins-faces2-higgsfield-original.png):
  the twins' eyes look straight ahead, Ada's mouth open. Each edited face is scaled back, lined up with the drawing
  (the shift that best matches the unchanged nose), its colours matched, and only where it differs inside AREA is
  laid on:
    evan-talk-higgsfield.png, milo-talk-higgsfield.png   the whole sprite with the new eyes (the old ones stay the
                                                         sprites for before they are spoken to)
    mouths/ada-talk-closed.png, mouths/ada-talk-open.png  Ada's talking sprite (ada-talk) as drawn / mouth open
  Prints the mouth box for MOUTHS.
"""
from PIL import Image, ImageChops, ImageDraw, ImageFilter
A = 'assets/characters/'; M = A + 'mouths/'
FACES = {'evan': (126, 60, 366, 300), 'milo': (122, 65, 362, 305), 'ada-talk': (50, 90, 290, 330)}
AREA = {'evan': (20, 20, 220, 100), 'milo': (20, 20, 220, 100), 'ada-talk': (75, 105, 190, 175)}   # in the 240 px face
NOSE = {'evan': (95, 75, 145, 120), 'milo': (95, 75, 145, 120), 'ada-talk': (95, 90, 135, 120)}   # unchanged, to line up

sheet = Image.open(M + 'twins-faces2-higgsfield-original.png').convert('RGB'); cw, ch = sheet.width / 3, sheet.height / 2

def mean_diff(a, b):
    d = ImageChops.difference(a, b).convert('L'); return sum(d.getdata()) / (d.size[0] * d.size[1])

for i, (key, face) in enumerate(FACES.items()):
    im = Image.open(A + key + '-higgsfield.png').convert('RGBA')
    flat = Image.new('RGBA', im.size, (255, 255, 255, 255)); flat.alpha_composite(im)
    src = flat.crop(face).convert('RGB'); n = src.size[0]
    cell = sheet.crop((round(i * cw), 0, round((i + 1) * cw), round(ch))).resize((n, n), Image.LANCZOS)
    # line up: the shift (dx, dy) whose nose matches the drawing best
    best = None
    for dx in range(-14, 15):
        for dy in range(-14, 15):
            sh = ImageChops.offset(cell, dx, dy); sc = mean_diff(src.crop(NOSE[key]), sh.crop(NOSE[key]))
            if best is None or sc < best[0]: best = (sc, dx, dy)
    ed = ImageChops.offset(cell, best[1], best[2])
    up = NOSE[key]; ms = [sum(c) / len(c) for c in zip(*src.crop(up).getdata())]; me = [sum(c) / len(c) for c in zip(*ed.crop(up).getdata())]
    ed = Image.merge('RGB', [c.point(lambda v, g=ms[j] / max(me[j], 1): min(255, round(v * g))) for j, c in enumerate(ed.split())])
    hit = ImageChops.difference(src, ed).convert('L').point(lambda v: 255 if v > 30 else 0)
    keep = Image.new('L', src.size, 0); ImageDraw.Draw(keep).rectangle(AREA[key], fill=255); hit = ImageChops.multiply(hit, keep)
    hit = hit.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(11))
    mask = ImageChops.multiply(hit.filter(ImageFilter.GaussianBlur(2.5)), keep.filter(ImageFilter.GaussianBlur(3)))
    layer = ed.convert('RGBA'); layer.putalpha(ImageChops.multiply(mask, im.crop(face).getchannel('A')))
    print(key, 'shift', best[1:], 'match', round(best[0], 1))
    if key in ('evan', 'milo'):
        out = im.copy(); out.alpha_composite(layer, face[:2]); out.save(f'{A}{key}-talk-higgsfield.png')
    else:
        tb = layer.getchannel('A').point(lambda v: 255 if v > 2 else 0).getbbox()
        box = [face[0] + tb[0], face[1] + tb[1], tb[2] - tb[0], tb[3] - tb[1]]
        mouth = layer.crop(tb); mouth.paste((0, 0, 0, 0), (0, 37, 33, 65))   # the sheet's white by her neck (user report 2026-11-25)
        mouth.save(M + 'ada-talk-open.png', optimize=True)
        im.crop((box[0], box[1], box[0] + box[2], box[1] + box[3])).save(M + 'ada-talk-closed.png', optimize=True)
        print('ada-talk mouth', box)

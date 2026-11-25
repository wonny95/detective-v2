"""The twins case's places (Case 06, design/case-twins.md), each from one tall 3:4 Higgsfield picture in
assets/places/twins/ (<id>-higgsfield-original.png): scaled to 1376 wide, a 1376-wide band of BAND px from TOP is the place (taller than 768, as the concert hall's lobby: more of it shows)
(<id>.webp), what is under it its floor (<id>-floor.jpg, ART_FLOOR), mirrored on to FLOOR_H.
- outside: job 0d1888e3-313a-407a-a157-910d966f2d5d (2 credits, 2026-11-25), the workshop and the found van
- road: job 17e13cc8-d3b6-4e2f-95a8-2680a708e23b, hospital: c11c0ab8-5769-4adf-95e4-ef71b06e2ba5, workshop:
  ab802042-8793-45f2-b0c6-7b054c742c81 (2 credits each, 2026-11-25)
Run from the project folder: python -I scripts/cut-twins-places.py"""
import colorsys
from PIL import Image, ImageFilter
D = 'assets/places/twins/'
FLOOR_H, BAND = 900, 1056


def bright_van(im):   # "A blue van" (2026-11-25): the drawn one is nearly navy; its blue a little brighter, nothing else
    x0, y0, x1, y1 = 925, 910, 1325, 1260
    v, m = im.crop((x0, y0, x1, y1)), Image.new('L', (x1 - x0, y1 - y0), 0)
    out, p, o, q = v.copy(), v.load(), None, m.load()
    o = out.load()
    for y in range(v.height):
        for x in range(v.width):
            r, g, b = p[x, y]
            h, s, l = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
            # by how blue it is, so greys (bumper, tyres, window) keep their colour without an edge
            w = max(0, min(1, (s - .1) / .16)) * (1 if .5 < h < .72 else 0)
            q[x, y] = round(255 * w)
            o[x, y] = tuple(round(c * 255) for c in colorsys.hsv_to_rgb(.585, min(1, s * 1.18), min(1, l * 1.32 + .05 * min(1, l * 2))))
    im.paste(out, (x0, y0), m.filter(ImageFilter.MedianFilter(3)).filter(ImageFilter.GaussianBlur(1.5)))
    return im


SRC = {'road': 'road-fixed.png'}   # scripts/fix-twins-road.py
for id, top in {'outside': 300, 'road': 380, 'hospital': 250, 'workshop': 300}.items():
    im = Image.open(D + SRC.get(id, f'{id}-higgsfield-original.png')).convert('RGB')
    im = im.resize((1376, round(im.height * 1376 / im.width)), Image.LANCZOS)
    if id == 'outside':
        im = bright_van(im)
    im.crop((0, top, 1376, top + BAND)).save(D + f'{id}.webp', quality=88)
    street = im.crop((0, top + BAND, 1376, im.height))
    floor = Image.new('RGB', (1376, FLOOR_H)); y, flip = 0, False
    while y < FLOOR_H:
        floor.paste(street.transpose(Image.FLIP_TOP_BOTTOM) if flip else street, (0, y)); y += street.height; flip = not flip
    floor.save(D + f'{id}-floor.jpg', quality=85)
    if id == 'outside':   # the case card: the workshop's window and the van
        im.crop((456, 560, 1376, 1400)).resize((920, 840)).save(D + 'cover.jpg', quality=88)
    print(id, im.size, 'floor h', street.height)

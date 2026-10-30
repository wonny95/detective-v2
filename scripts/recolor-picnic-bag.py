"""Rosie's bag as Nora hands it back (0 credits): picnic.webp with the green lunch box made red and the blue bottle made
yellow, by hue swaps inside the shapes of the two things only -> picnic-rosie-bag.webp"""
import colorsys, sys
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('RGB'); px = im.load()
def swap(box, inside, test, hue, sat_mul=1.0, lift=0.0, gain=1.0):
    x0, y0, x1, y1 = box
    for y in range(y0, y1):
        for x in range(x0, x1):
            if not inside(x, y): continue
            h, s, v = colorsys.rgb_to_hsv(*(c / 255 for c in px[x, y]))
            if test(h * 360, s, v):
                rgb = colorsys.hsv_to_rgb(hue / 360, min(1, s * sat_mul), min(1, v * gain + lift))
                px[x, y] = tuple(round(c * 255) for c in rgb)
everywhere = lambda x, y: True
# lunch box: green -> tomato red
swap((872, 388, 994, 462), everywhere, lambda h, s, v: 60 <= h <= 170 and s > .22, 2, 1.3, 0, 1.08)
# bottle body (an ellipse) and cap (a box); the bag's blue-grey around them is left alone
body = lambda x, y: ((x - 1013) / 27) ** 2 + ((y - 432) / 24) ** 2 <= 1
cap = lambda x, y: ((x - 1019) / 15.5) ** 2 + ((y - 398) / 11) ** 2 <= 1
swap((985, 405, 1042, 460), body, lambda h, s, v: 190 <= h <= 250 and s > .2 and v > .4, 50, 1.4, .08, 1.3)
swap((1003, 386, 1037, 411), cap, lambda h, s, v: 190 <= h <= 250 and s > .25, 44, 1.3, .05, 1.25)
im.save(out)

# The twins' interview pictures (design/case-twins.md): one Higgsfield picture (assets/places/twins/
# interview-evan-higgsfield-original.png), the scratch moved by hand here so the two are the same but for it.
# Evan: his right wrist (left on the screen). Milo: his left index finger (right on the screen).
# Run: python scripts/make-twins-interview.py
from PIL import Image, ImageDraw, ImageFilter
import os
D = os.path.join(os.path.dirname(__file__), '..', 'assets', 'places', 'twins')
src = Image.open(os.path.join(D, 'interview-evan-higgsfield-original.png')).convert('RGB')
AXIS = 916   # the arms mirror about x 458

# the drawn scratch taken off: that bit of the arm covered with the other arm's, mirrored, with a soft edge
box = (526, 782, 574, 832)
patch = src.crop((AXIS - box[2], box[1], AXIS - box[0], box[3])).transpose(Image.FLIP_LEFT_RIGHT)
mask = Image.new('L', patch.size, 0)
ImageDraw.Draw(mask).ellipse((4, 4, patch.size[0] - 5, patch.size[1] - 5), fill=255)
clean = src.copy()
clean.paste(patch, box[:2], mask.filter(ImageFilter.GaussianBlur(3)))

# a tapered stroke (thin ends), with a darker edge, as the crayon scratch was
def scratch(img, strokes):
    S = 6
    big = Image.new('RGBA', (img.width * S, img.height * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(big)
    for (x0, y0, x1, y1, w) in strokes:
        for extra, colour in ((1.0, (110, 24, 22, 170)), (0, (200, 44, 44, 255))):
            for i in range(61):
                t = i / 60
                r = (w * (1 - (2 * t - 1) ** 2) ** .6 + extra) / 2 * S
                x, y = (x0 + (x1 - x0) * t) * S, (y0 + (y1 - y0) * t) * S
                d.ellipse((x - r, y - r, x + r, y + r), fill=colour)
    out = img.convert('RGBA')
    out.alpha_composite(big.resize(img.size, Image.LANCZOS))
    return out.convert('RGB')

evan = scratch(clean, [(362, 827, 384, 840, 2.6), (371, 840, 381, 846, 1.2)])
milo = scratch(clean, [(501, 869, 508, 877, 2.4)])
for name, img in (('evan', evan), ('milo', milo)):
    img.save(os.path.join(D, f'interview-{name}.png'))

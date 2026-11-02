"""The blue backpack handed over in the picnic case's ending (user request: a real bag, not a photo of it), cut with no
credits from one Higgsfield picture on flat green (bag-blue-higgsfield-original.png, Nano Banana 2.1, job
4514fe11-d4ea-4c01-9e46-395525df8c15, the picnic table's backpack as the reference): the green keyed out (also through
the carry loop), green spill on the edge taken off, trimmed with a small margin and scaled to 420 px tall
-> assets/places/picnic-storyboard/bag-blue.png. Rosie's and Nora's bags look the same, so both use it."""
from PIL import Image, ImageFilter
D = 'assets/places/picnic-storyboard/'
im = Image.open(D + 'bag-blue-higgsfield-original.png').convert('RGB')
px = im.load(); W, H = im.size
alpha = Image.new('L', im.size); ap = alpha.load()
out = Image.new('RGBA', im.size); op = out.load()
for y in range(H):
    for x in range(W):
        r, g, b = px[x, y]
        green = g - max(r, b)               # how far it leans to the key green
        a = 255 if green < 40 else 0 if green > 120 else round(255 * (120 - green) / 80)
        ap[x, y] = a
        g = min(g, max(r, b) + 12)          # no green fringe
        # the canvas came out grey-green: toward the picnic table backpack's blue (its R:G:B about .80:.91:1); the tan
        # straps and the brown outline (red over blue) stay
        if b >= r - 4 and g >= r - 4: r, g = round(r * .84), round(g * .875)
        op[x, y] = (r, g, b, a)
# soften the cut edge a little, as the drawing's own crayon edge
a = out.getchannel('A').filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(.8))
out.putalpha(a)
box = a.point(lambda v: 255 if v > 16 else 0).getbbox()
out = out.crop(box); m = round(max(out.size) * .03)
pad = Image.new('RGBA', (out.width + 2 * m, out.height + 2 * m)); pad.paste(out, (m, m))
s = 420 / pad.height
pad.resize((round(pad.width * s), 420), Image.LANCZOS).save(D + 'bag-blue.png', optimize=True)
print('bag-blue.png', round(pad.width * s), 420)

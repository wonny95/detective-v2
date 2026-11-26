# The case folder's parts and the mini-game strip for the case list, out of
# assets/ui/case-folder-parts-v3-higgsfield-original.png (Higgsfield nano_banana_2_1 16:9, job
# b724c3b9-8a99-4b1f-a55b-27dc03ddcdf3, magenta background; user request 2026-11-26: thin outlines, a strip with no folded
# corner that stretches sideways):
#   case-folder-front.webp (the cover from outside), case-folder-inside.webp (the cover's inner side, mirrored so its crease
#   lies on the hinge once turned over), case-folder-paper.webp (the sheet). (The mini-game strip it also gave is no longer used: the games are folders too,
#   user pick 2026-11-26.)
#   case-folder-back.webp (the back with its index tab): the new sheet drew the tab on the back's left side, so (user choice)
#   the back is made here: the shape of the earlier back (tab on top left, from case-folder-parts-higgsfield-original.png,
#   job 4a1d19fe) filled with the new cover's kraft and outlined with the new cover's thin line colour.
from PIL import Image, ImageOps, ImageFilter, ImageChops
D = 'assets/ui/'
def keyer(path):
    S = Image.open(D + path).convert('RGB'); BG = S.getpixel((1370, 760)); K = min(BG[0], BG[2]) - BG[1]
    def key(box):
        i = S.crop(box).convert('RGBA'); p = i.load()
        for y in range(i.height):
            for x in range(i.width):
                r, g, b, _ = p[x, y]
                a = 1 - max(0, min(1, (min(r, b) - g - 6) / (K - 26)))
                if a <= .04: p[x, y] = (0, 0, 0, 0); continue
                c = [max(0, min(255, round((v - (1 - a) * q) / a))) for v, q in zip((r, g, b), BG)]
                if a < 1: c[2] = min(c[2], c[1])   # no pink left in the brown outline
                p[x, y] = (*c, round(a * 255))
        return depink(i.crop(i.getchannel('A').point(lambda v: 255 if v > 40 else 0).getbbox()))
    return key
LINE = (140, 100, 78)   # the thin brown pencil line; the sheet's outline came out pink where it met the magenta
def depink(i):
    p = i.load()
    for y in range(i.height):
        for x in range(i.width):
            r, g, b, a = p[x, y]
            if a and r - g > 40 and b > g - 15:   # pink-tinted outline pixel -> the line brown, as dark as it was
                k = min(1, (r + g + b) / 3 / 150); p[x, y] = (*(round(c * k) for c in LINE), a)
    return i
new = keyer('case-folder-parts-v3-higgsfield-original.png')
front = new((15, 15, 345, 480))
inside = ImageOps.mirror(new((354, 15, 686, 480))).resize(front.size, Image.LANCZOS)
paper = new((1045, 15, 1360, 480))
strip = new((15, 490, 950, 760))
# the back: the old back's shape at the new cover's width (the cover is 90.5% of the back's height, as the CSS lays it)
old = keyer('case-folder-parts-higgsfield-original.png')((690, 25, 1037, 540))
bw = front.width; bh = round(front.height / .905)
mask = old.getchannel('A').resize((bw, bh), Image.LANCZOS)
inner = front.crop((14, 14, front.width - 14, front.height - 14)).convert('RGB')
fill = inner.resize((bw, bh), Image.LANCZOS)
edge = LINE
ring = ImageChops.subtract(mask, mask.filter(ImageFilter.MinFilter(5)))
back = Image.new('RGBA', (bw, bh)); back.paste(fill, (0, 0)); back.putalpha(mask)
line = Image.new('RGBA', (bw, bh), (*edge, 255)); line.putalpha(ring)
back = Image.alpha_composite(back, line)
for name, i in (('folder-front', front), ('folder-inside', inside), ('folder-back', back), ('folder-paper', paper)):
    i.save(f'{D}case-{name}.webp', quality=92, method=6); print(name, i.size)
print('line', edge)

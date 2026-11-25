# The case folder's parts out of assets/ui/case-folder-parts-higgsfield-original.png (Higgsfield nano_banana_2_1 16:9,
# job 4a1d19fe-c0ae-49dd-91ab-6c5c24215058, magenta background), so the cover can turn on its own over the paper:
# case-folder-front.webp (the cover from outside), case-folder-inside.webp (the cover's inner side, mirrored so its crease
# lies on the hinge once turned over), case-folder-back.webp (the back with the tab) and case-folder-paper.webp (the sheet).
from PIL import Image, ImageOps
D = 'assets/ui/'
S = Image.open(D + 'case-folder-parts-higgsfield-original.png').convert('RGB')
BG = S.getpixel((5, 700))
K = min(BG[0], BG[2]) - BG[1]
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
    return i.crop(i.getchannel('A').point(lambda v: 255 if v > 40 else 0).getbbox())
front = key((15, 60, 356, 540))
inside = ImageOps.mirror(key((356, 60, 690, 540))).resize(front.size, Image.LANCZOS)
back = key((690, 25, 1037, 540))
paper = key((1037, 60, 1365, 540))
for name, i in (('front', front), ('inside', inside), ('back', back), ('paper', paper)):
    i.save(f'{D}case-folder-{name}.webp', quality=92, method=6); print(name, i.size)

# The case list's blank folders out of assets/ui/case-folders-higgsfield-original.png (Higgsfield, magenta background):
# case-folder-wide.webp and case-folder-tall.webp. The paperclip on the sheet is drawn broken and is not used.
from PIL import Image
D = 'assets/ui/'
S = Image.open(D + 'case-folders-higgsfield-original.png').convert('RGB')
BG = S.getpixel((5, 5))
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
for name, box in (('wide', (60, 10, 980, 475)), ('tall', (60, 470, 540, 1010))):
    i = key(box); i.save(f'{D}case-folder-{name}.webp', quality=92, method=6); print(name, i.size)

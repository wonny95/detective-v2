"""Cut the 이번 사건의 열쇠 paper pieces (assets/ui/casekey-pieces-higgsfield-original.png, on magenta) into
assets/ui/casekey/: the key card, the yellow / blue / pink notes and a piece of tape, each cropped to its drawing;
and a repeating graph-paper tile from the middle of assets/ui/graph-paper-higgsfield-original.png (8 x 8 squares,
cut halfway between pencil lines so the lines carry on across the seams)."""
import os
from PIL import Image

def key(im):
    W, H = im.size
    out = Image.new('RGBA', im.size)
    src, dst = im.load(), out.load()
    for y in range(H):
        for x in range(W):
            r, g, b = src[x, y]
            k = min(r, b) - g                      # 255 on pure magenta, below 0 on the drawing
            a = 1.0 if k < 60 else 0.0 if k > 170 else (170 - k) / 110
            if a <= 0: dst[x, y] = (0, 0, 0, 0); continue
            if a < 1:                              # un-mix the magenta from the edge
                r = (r - (1 - a) * 255) / a; b = (b - (1 - a) * 255) / a
            dst[x, y] = (max(0, min(255, round(r))), g, max(0, min(255, round(b))), round(a * 255))
    return out

os.makedirs('assets/ui/casekey', exist_ok=True)
sheet = key(Image.open('assets/ui/casekey-pieces-higgsfield-original.png').convert('RGB'))
# rough regions on the 1264 x 848 sheet; each is cropped to its drawing with a 2px margin
REGIONS = {'card': (0, 0, 1264, 440), 'note-yellow': (0, 440, 760, 570), 'note-blue': (0, 570, 760, 690),
           'note-pink': (0, 690, 760, 848), 'tape': (760, 470, 1264, 630)}
for name, box in REGIONS.items():
    part = sheet.crop(box)
    l, t, r, b = part.getchannel('A').point(lambda v: 255 if v > 64 else 0).getbbox()
    part = part.crop((max(0, l - 2), max(0, t - 2), r + 2, b + 2))
    if name == 'card': part = part.resize((part.width // 2, part.height // 2), Image.LANCZOS)
    part.save(f'assets/ui/casekey/{name}.webp', quality=92)
    print(name, part.size)

paper = Image.open('assets/ui/graph-paper-higgsfield-original.png').convert('RGB')
tile = paper.crop((238, 286, 635, 688)).resize((352, 352), Image.LANCZOS)
tile.save('assets/ui/casekey/graph-paper.webp', quality=90)
print('graph-paper', tile.size)

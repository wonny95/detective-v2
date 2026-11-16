"""Cut the deduction board's O/X sticky notes out of the Higgsfield sheet (assets/ui/deduce-notes-higgsfield-original.png,
four notes stacked on magenta) into assets/ui/deduce-note-<1..4>.webp, the magenta keyed out as in
scripts/cut-casekey-pieces.py. Run from the project folder: python scripts/cut-deduce-notes.py"""
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

sheet = key(Image.open('assets/ui/deduce-notes-higgsfield-original.png').convert('RGB'))
W, H = sheet.size
mask = sheet.getchannel('A').point(lambda v: 255 if v > 64 else 0)
# the rows that hold a note (more than a third of the row drawn), in runs: one run per note
px = mask.load()
full = [sum(1 for x in range(0, W, 4) if px[x, y]) * 4 > W / 3 for y in range(H)]
runs, start = [], None
for y, on in enumerate(full + [False]):
    if on and start is None: start = y
    if not on and start is not None: runs.append((start, y)); start = None
for n, (t, b) in enumerate(runs, 1):
    part = sheet.crop((0, max(t - 6, 0), W, min(b + 6, H)))
    l, tt, r, bb = part.getchannel('A').point(lambda v: 255 if v > 64 else 0).getbbox()
    part = part.crop((max(l - 2, 0), max(tt - 2, 0), r + 2, bb + 2))
    part.save(f'assets/ui/deduce-note-{n}.webp', quality=92)
    print(n, part.size)

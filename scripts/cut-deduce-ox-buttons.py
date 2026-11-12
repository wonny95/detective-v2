"""Cut the deduction board's O/X answer buttons out of the Higgsfield sheet
(assets/ui/deduce-ox-buttons-higgsfield-original.png: 4 rows of buttons on magenta, each row one style,
O X O X across) into assets/ui/deduce-ox-<style>-<o|x>.webp, the first O and X of each row.
The magenta is keyed out as in scripts/cut-deduce-notes.py. Run from the project folder."""
from PIL import Image

def key(im):
    out = Image.new('RGBA', im.size)
    src, dst = im.load(), out.load()
    W, H = im.size
    for y in range(H):
        for x in range(W):
            r, g, b = src[x, y]
            k = min(r, b) - g
            a = 1.0 if k < 60 else 0.0 if k > 170 else (170 - k) / 110
            if a <= 0: dst[x, y] = (0, 0, 0, 0); continue
            if a < 1:
                r = (r - (1 - a) * 255) / a; b = (b - (1 - a) * 255) / a
            m = min(r, b)                          # despill: no pink left on the rim
            if m > g: r -= m - g; b -= m - g
            dst[x, y] = (max(0, min(255, round(r))), g, max(0, min(255, round(b))), round(a * 255))
    return out

sheet = key(Image.open('assets/ui/deduce-ox-buttons-higgsfield-original.png').convert('RGB'))
W, H = sheet.size
for row, style in enumerate(['wood', 'paper', 'wax', 'badge']):
    for col, mark in enumerate('ox'):
        cell = sheet.crop((col * W // 4, row * H // 4, (col + 1) * W // 4, (row + 1) * H // 4))
        # keep only the button in the middle of the cell (slivers of the neighbours reach into it)
        cw, ch = cell.size; px = cell.load(); seen = set(); todo = [(cw // 2, ch // 2)]
        while todo:
            x, y = todo.pop()
            if (x, y) in seen or not (0 <= x < cw and 0 <= y < ch) or px[x, y][3] <= 8: continue
            seen.add((x, y)); todo += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for y in range(ch):
            for x in range(cw):
                if (x, y) not in seen: px[x, y] = (0, 0, 0, 0)
        l, t, r, b = cell.getchannel('A').point(lambda v: 255 if v > 48 else 0).getbbox()
        part = cell.crop((max(l - 2, 0), max(t - 2, 0), r + 2, b + 2))
        part.thumbnail((160, 160), Image.LANCZOS)
        part.save(f'assets/ui/deduce-ox-{style}-{mark}.webp', quality=92)
        print(style, mark, part.size)

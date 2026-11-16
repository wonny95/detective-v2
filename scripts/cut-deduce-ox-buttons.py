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
# each button is the drawn blob around its grid cell's centre, found on the whole sheet (a button can reach past
# its quarter of the sheet; cutting by the grid clipped the badge O's edge)
px = sheet.load()
for row, style in enumerate(['wood', 'paper', 'wax', 'badge']):
    for col, mark in enumerate('ox'):
        seen = set(); todo = [(col * W // 4 + W // 8, row * H // 4 + H // 8)]
        while todo:
            x, y = todo.pop()
            if (x, y) in seen or not (0 <= x < W and 0 <= y < H) or px[x, y][3] <= 8: continue
            seen.add((x, y)); todo += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        xs = [x for x, _ in seen]; ys = [y for _, y in seen]
        box = (min(xs) - 2, min(ys) - 2, max(xs) + 3, max(ys) + 3)
        part = Image.new('RGBA', (box[2] - box[0], box[3] - box[1]))
        pp = part.load()
        for x, y in seen: pp[x - box[0], y - box[1]] = px[x, y]
        part.thumbnail((160, 160), Image.LANCZOS)
        part.save(f'assets/ui/deduce-ox-{style}-{mark}.webp', quality=92)
        print(style, mark, part.size)

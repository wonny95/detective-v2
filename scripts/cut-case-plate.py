"""Cut the four case-number plate candidates out of the Higgsfield sheet (2026-11-19, job 6f11bf3d).

assets/ui/case-plate-higgsfield-original.png is a 2x2 sheet on white: 1 dark wood with a gold line, 2 brass plate,
3 light board with nails, 4 red ribbon. Each quarter's white background (the part joined to the quarter's edge) is
made transparent, the plate is cropped to its box and scaled to 480 px wide -> assets/ui/case-plate-<n>.webp.
"""
from collections import deque
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'assets/ui/case-plate-higgsfield-original.png'
OUT_W = 480


def cut(im):
    im = im.convert('RGBA')
    w, h = im.size
    px = im.load()
    white = lambda p: min(p[:3]) > 232
    seen = bytearray(w * h)
    q = deque((x, y) for x in range(w) for y in (0, h - 1))
    q.extend((x, y) for y in range(h) for x in (0, w - 1))
    while q:
        x, y = q.popleft()
        i = y * w + x
        if seen[i] or not white(px[x, y]):
            continue
        seen[i] = 1
        px[x, y] = (255, 255, 255, 0)
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < w and 0 <= ny < h and not seen[ny * w + nx]:
                q.append((nx, ny))
    # soften the light fringe left round the outline: near-white pixels touching transparency get half alpha
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            p = px[x, y]
            if p[3] and min(p[:3]) > 205 and any(px[x + dx, y + dy][3] == 0 for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                px[x, y] = p[:3] + (110,)
    return im.crop(im.getbbox())


def main():
    sheet = Image.open(SRC)
    W, H = sheet.size
    for n, (cx, cy) in enumerate(((0, 0), (1, 0), (0, 1), (1, 1)), 1):
        part = cut(sheet.crop((cx * W // 2, cy * H // 2, (cx + 1) * W // 2, (cy + 1) * H // 2)))
        part = part.resize((OUT_W, round(part.height * OUT_W / part.width)), Image.LANCZOS)
        out = ROOT / f'assets/ui/case-plate-{n}.webp'
        part.save(out, 'WEBP', quality=90, method=6)
        print(out.name, part.size)


if __name__ == '__main__':
    main()

"""Word-matching game icon options (user request 2026-11-23: the CSS cork board looked odd; four candidates on one sheet,
Nano Banana 2.1 16:9 2K, job 57740533-938e-4db3-b7bd-9801816e569b, the safe icon as style reference, flat magenta)
-> assets/ui/match-icons-higgsfield-original.png. Magenta keyed out (as scripts/cut-pablo.py), split at the empty
columns, trimmed with a 3% margin, scaled to 400 wide (the safe icon's width) -> design/match-icon-options/<n>.png:
1 cork board with string, 2 puzzle pieces, 3 clipped flash cards, 4 open notebook.
Run from the project folder: python -I scripts/cut-match-icons.py"""
import os
from PIL import Image, ImageFilter
src = Image.open('assets/ui/match-icons-higgsfield-original.png').convert('RGB')
OUT = 'design/match-icon-options/'; os.makedirs(OUT, exist_ok=True)
def key_out(img):
    px = img.load(); W0, H0 = img.size
    rgba = img.convert('RGBA'); rp = rgba.load(); alpha = Image.new('L', img.size); ap = alpha.load()
    for y in range(H0):
        for x in range(W0):
            r, g, b = px[x, y]; k = max(0, min(r, b) - g)
            a = 255 if k < 60 else 0 if k > 150 else round(255 * (150 - k) / 90)
            ap[x, y] = a
            if 0 < a < 255 or (a == 255 and k > 25):
                rp[x, y] = (min(r, g + 40) if r > g + 40 else r, g, min(b, g + 40) if b > g + 40 else b, 255)
    rgba.putalpha(alpha.filter(ImageFilter.GaussianBlur(.6)))
    return rgba
for n, (x0, x1) in enumerate([(100, 712), (788, 1402), (1454, 1939), (2021, 2668)], 1):
    fig = key_out(src.crop((x0, 0, x1, src.height)))
    fig = fig.crop(fig.getchannel('A').point(lambda a: 255 if a > 24 else 0).getbbox())
    m = round(max(fig.size) * .03)
    out = Image.new('RGBA', (fig.width + 2 * m, fig.height + 2 * m)); out.paste(fig, (m, m))
    s = 400 / out.width; out = out.resize((400, round(out.height * s)), Image.LANCZOS)
    out.save(OUT + f'{n}.png', optimize=True)
    print(n, out.size)

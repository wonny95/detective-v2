"""Cut the spelling-safe sheet (assets/ui/safe-cutout-original.png, Higgsfield 2026-11-23, background removed)
into the closed and the open safe for the case board: safe-closed / safe-open (.png and .webp), 400px wide."""
from PIL import Image
src = Image.open('assets/ui/safe-cutout-original.png').convert('RGBA')
W, H = src.size
for name, box in (('safe-closed', (0, 0, W // 2, H)), ('safe-open', (W // 2, 0, W, H))):
    im = src.crop(box)
    im = im.crop(im.getchannel('A').point(lambda a: 255 if a > 20 else 0).getbbox())
    pad = 8
    out = Image.new('RGBA', (im.width + 2 * pad, im.height + 2 * pad))
    out.paste(im, (pad, pad))
    out = out.resize((400, round(out.height * 400 / out.width)), Image.LANCZOS)
    out.save(f'assets/ui/{name}.png')
    out.save(f'assets/ui/{name}.webp', quality=90)
    print(name, out.size)

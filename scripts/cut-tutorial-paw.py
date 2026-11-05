"""Cut the tutorial's tap pointer, the detective's right paw seen from the back (user decision: 오른손 2), from the
Higgsfield sheet assets/ui/pointer-paws-back-higgsfield-original.png (six paws 3x2 on magenta, a LEFT paw from behind):
the top middle one, alpha by how magenta a pixel is (as cut-nudge-marks.py), cropped to the drawing with a 4px margin,
the longer side 200px, then mirrored into a right paw -> assets/ui/tutorial-paw.png. Prints where the fingertip is (the
top of the drawing, as a fraction of the width), which the tutorial lines up with the spot it taps."""
from PIL import Image, ImageOps

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

out = key(Image.open('assets/ui/pointer-paws-back-higgsfield-original.png').convert('RGB'))
W, H = out.size
cell = out.crop((W // 3, 0, 2 * W // 3, H // 2))          # top row, middle
l, t, r, b = cell.getchannel('A').point(lambda v: 255 if v > 64 else 0).getbbox()
part = cell.crop((max(0, l - 4), max(0, t - 4), r + 4, b + 4))
s = 200 / max(part.size)
part = ImageOps.mirror(part.resize((round(part.width * s), round(part.height * s)), Image.LANCZOS))
a = part.getchannel('A')
top = next(y for y in range(part.height) if any(a.getpixel((x, y)) > 128 for x in range(part.width)))
xs = [x for x in range(part.width) if a.getpixel((x, top + 6)) > 128]
part.save('assets/ui/tutorial-paw.png', optimize=True)
print('tutorial-paw', part.size, 'tip x', round((xs[0] + xs[-1]) / 2 / part.width, 3))

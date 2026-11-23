"""Gus's sneeze and sorry faces (user request 2026-11-23, flowerbed case): one Higgsfield sheet, Nano Banana 2.1 16:9 2K,
job 9b3266c2-1c7d-420c-bc11-856abfdd68bb, the Ollie/Gus sheet as reference, on flat magenta
-> assets/characters/gus-moods-higgsfield-original.png: left sneezing (eyes shut, mouth wide open), right sorry.
Magenta keyed out as scripts/cut-pablo.py, split at the empty column, 3% margin, 700 px tall
-> gus-sneeze.png/.webp, gus-sorry.png/.webp. Prints sizes; SPRITES 'gus:sneeze' / 'gus:sorry' take `height` relative
to the base sprite so the soccer ball comes out the same size (measured on the ball, see HEIGHT below).
Run from the project folder: python -I scripts/cut-gus-moods.py"""
from PIL import Image, ImageFilter
D = 'assets/characters/'
src = Image.open(D + 'gus-moods-higgsfield-original.png').convert('RGB')
SPLIT = 1420
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
def save(name, part):
    im = key_out(part)
    box = im.getchannel('A').point(lambda a: 255 if a > 24 else 0).getbbox()
    im = im.crop(box); m = round(max(im.size) * .03)
    out = Image.new('RGBA', (im.width + 2 * m, im.height + 2 * m)); out.paste(im, (m, m))
    s = 700 / out.height; out = out.resize((round(out.width * s), 700), Image.LANCZOS)
    out.save(D + f'{name}.png', optimize=True); out.save(D + f'{name}.webp', quality=90)
    print(name, out.size, 'figure px in sheet', box[3] - box[1])
# the sneeze is drawn with the tail on the left: mirrored so the tail is on the right, as his other pictures
save('gus-sneeze', src.crop((0, 0, SPLIT, src.height)).transpose(Image.FLIP_LEFT_RIGHT))
save('gus-sorry', src.crop((SPLIT, 0, src.width, src.height)))

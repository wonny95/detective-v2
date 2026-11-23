"""Pablo Panda, the flowerbed case's tennis-ball friend (user decision 2026-11-23: a new character instead of Toby Bear in
this case; Toby stays in the kite and montage cases). Higgsfield Nano Banana 2.1, 3:4 1K, job d7cfa603-1a3b-4998-a7e3-4aaa69e42a60,
the Ollie/Gus sheet as style reference, on flat magenta (white panda fur would not key out of white)
-> assets/characters/pablo-higgsfield-original.png.
Magenta keyed out (soft edge, the pink left on the outline pulled back to the paper's ink colour), 3% margin, 700 px tall
-> assets/characters/pablo-higgsfield.png/.webp, and a 160 px face icon -> assets/ui/icons-v2/pablo.png/.webp.
Prints the sprite size and the face viewBox for SPRITES. Run from the project folder: python -I scripts/cut-pablo.py"""
from PIL import Image, ImageFilter
D = 'assets/characters/'
src = Image.open(D + 'pablo-higgsfield-original.png').convert('RGB')
W0, H0 = src.size
# how magenta a pixel is: red and blue high, green low
def keyness(p):
    r, g, b = p
    return max(0, min(r, b) - g)
px = src.load()
alpha = Image.new('L', src.size); ap = alpha.load()
rgba = src.convert('RGBA'); rp = rgba.load()
for y in range(H0):
    for x in range(W0):
        k = keyness(px[x, y])
        a = 255 if k < 60 else 0 if k > 150 else round(255 * (150 - k) / 90)
        ap[x, y] = a
        if 0 < a < 255 or (a == 255 and k > 25):          # despill: pull the magenta out of the edge pixels
            r, g, b = px[x, y]; m = min(r, b)
            rp[x, y] = (min(r, g + 40) if r > g + 40 else r, g, min(b, g + 40) if b > g + 40 else b, 255)
alpha = alpha.filter(ImageFilter.GaussianBlur(.6))
rgba.putalpha(alpha)
box = alpha.point(lambda a: 255 if a > 24 else 0).getbbox()
im = rgba.crop(box); m = round(max(im.size) * .03)
out = Image.new('RGBA', (im.width + 2 * m, im.height + 2 * m)); out.paste(im, (m, m)); im = out
s = 700 / im.height
im = im.resize((round(im.width * s), 700), Image.LANCZOS)
im.save(D + 'pablo-higgsfield.png', optimize=True); im.save(D + 'pablo-higgsfield.webp', quality=90)
W, H = im.size
# the head: the widest run of the top half
head = im.crop((0, 0, W, round(H * .45))).getchannel('A').point(lambda v: 255 if v > 40 else 0).getbbox()
side = round(.46 * H); cx = (head[0] + head[2]) // 2; y0 = round(.02 * H)
print('pablo', im.size, f"face:'{cx - side // 2} {y0} {side} {side}'")
face = Image.new('RGBA', (side, side)); face.paste(im.crop((cx - side // 2, y0, cx - side // 2 + side, y0 + side)), (0, 0))
icon = Image.new('RGBA', (160, 160)); icon.paste(face.resize((148, 148), Image.LANCZOS), (6, 6))
rim = icon.getchannel('A').point(lambda v: 255 if v > 40 else 0).filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.GaussianBlur(.8))
white = Image.new('RGBA', (160, 160), (255, 255, 255, 255)); white.putalpha(rim)
white.alpha_composite(icon); white.save('assets/ui/icons-v2/pablo.png', optimize=True); white.save('assets/ui/icons-v2/pablo.webp', quality=90)

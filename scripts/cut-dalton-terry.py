"""Dalton (mouse, the player's detective) and Terry (cat, the police officer), user decision 2026-11-19: they take the place
of the squirrel detective and Sgt. Badger (whose pictures stay on disk). Background removed by Higgsfield:
  dalton-terry-v3-cutout.png  (job 3ba5d28c-…, from dalton-terry-v3-police-higgsfield-original.png): Dalton's default pose
                              (left) and Terry (right)
  dalton-poses-cutout.png     (job 3e1600d0-…, from dalton-poses-higgsfield-original.png): thinking, point, lens, wave;
                              used through dalton-poses-doteyes-cutout.png (dot eyes, scripts/make-dalton-doteyes.py)
Each is cropped with a 3% margin, scaled to 700 px tall -> assets/characters/<name>.png, plus the 160 px face icons
assets/ui/icons-v2/dalton.png, terry.png. Prints sizes and face viewBoxes for SPRITES.
Run: python -I scripts/make-dalton-doteyes.py ; python -I scripts/cut-dalton-terry.py   (Pillow only; writes .png and .webp)"""
from PIL import Image, ImageFilter
D = 'assets/characters/'
def trim(im):
    box = im.getchannel('A').point(lambda a: 255 if a > 24 else 0).getbbox()
    im = im.crop(box); m = round(max(im.size) * .03)
    out = Image.new('RGBA', (im.width + 2 * m, im.height + 2 * m)); out.paste(im, (m, m)); return out
def save(name, im, icon=None, head=None):
    """head: (centre x, top, side) as shares of the sprite's width/height, for the face viewBox and the icon"""
    im = trim(im); s = 700 / im.height
    im = im.resize((round(im.width * s), 700), Image.LANCZOS)
    im.save(D + f'{name}.png', optimize=True); im.save(D + f'{name}.webp', quality=90)
    W, H = im.size; cx, y0, side = round(head[0] * W), round(head[1] * H), round(head[2] * H)
    print(name, im.size, f"face:'{cx - side // 2} {y0} {side} {side}'")
    if not icon: return
    face = Image.new('RGBA', (side, side)); face.paste(im.crop((cx - side // 2, y0, cx + side - side // 2, y0 + side)), (0, 0))
    ic = Image.new('RGBA', (160, 160)); ic.paste(face.resize((148, 148), Image.LANCZOS), (6, 6))
    rim = ic.getchannel('A').point(lambda v: 255 if v > 40 else 0).filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.GaussianBlur(.8))
    white = Image.new('RGBA', (160, 160), (255, 255, 255, 255)); white.putalpha(rim)
    white.alpha_composite(ic); white.save(f'assets/ui/icons-v2/{icon}.png', optimize=True); white.save(f'assets/ui/icons-v2/{icon}.webp', quality=90)

pair = Image.open(D + 'dalton-terry-v3-cutout.png').convert('RGBA')
save('dalton', pair.crop((0, 0, 717, pair.height)), 'dalton', (.5, .0, .56))
save('terry', pair.crop((717, 0, pair.width, pair.height)), 'terry', (.5, .0, .56))

sheet = Image.open(D + 'dalton-poses-doteyes-cutout.png').convert('RGBA')   # dot eyes: scripts/make-dalton-doteyes.py (2026-11-23)
# the second and third poses overlap in x (the pointing finger under the third one's whiskers): split that strip by height
def part(x0, x1, keep):
    out = Image.new('RGBA', sheet.size); px, src = out.load(), sheet.load()
    for y in range(sheet.height):
        for x in range(x0, x1):
            if keep(x, y): px[x, y] = src[x, y]
    return out.crop((x0, 0, x1, sheet.height))
mid2 = lambda x, y: x < 1380 or (x < 1480 and y >= 715 and x < 1440)
save('dalton-thinking', sheet.crop((0, 0, 731, sheet.height)), None, (.5, .0, .56))
save('dalton-point', part(731, 1480, mid2), None, (.5, .0, .56))
save('dalton-lens', part(1380, 2027, lambda x, y: not mid2(x, y)), None, (.5, .0, .56))
save('dalton-wave', sheet.crop((2027, 0, sheet.width, sheet.height)), None, (.5, .0, .56))

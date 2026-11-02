"""Picnic case people from the two Higgsfield sheets (two per sheet, user decision), background already removed by
Higgsfield (`*-cutout.webp`): Ben (left) and Nora (right) cut apart, Mia & Ollie kept together as one figure (one person
in the game, `mia`). Each is cropped to its drawing with a 3% margin and scaled to 700 px tall like the other sprites
-> assets/characters/<id>-higgsfield.png. Also a 160 px face icon (head and shoulders, white rim as the icons-v2 sheet)
-> assets/ui/icons-v2/<id>.png. Prints each sprite's size and the face viewBox for SPRITES."""
from PIL import Image, ImageFilter
D = 'assets/characters/'
def trim(im):
    box = im.getchannel('A').point(lambda a: 255 if a > 24 else 0).getbbox()
    im = im.crop(box); m = round(max(im.size) * .03)
    out = Image.new('RGBA', (im.width + 2 * m, im.height + 2 * m)); out.paste(im, (m, m)); return out
def square(im, cx, y0, side):
    face = Image.new('RGBA', (side, side)); face.paste(im.crop((round(cx - side / 2), y0, round(cx + side / 2), y0 + side)), (0, 0))
    return face
def save(id, im, heads, sprite=True):
    """heads: [(centre x, top, side)] as shares of the sprite's width/height; one head fills the icon, two overlap.
    sprite=False makes only the face icon"""
    im = trim(im); s = 700 / im.height
    im = im.resize((round(im.width * s), 700), Image.LANCZOS)
    if sprite: im.save(D + f'{id}-higgsfield.png', optimize=True)
    W, H = im.size; boxes = [(round(x * W), round(y * H), round(z * H)) for x, y, z in heads]
    cx, y0, side = boxes[0]
    print(id, im.size, f"face:'{round(cx - side / 2)} {y0} {side} {side}'")
    icon = Image.new('RGBA', (160, 160))
    if len(boxes) == 1: icon.paste(square(im, *boxes[0]).resize((148, 148), Image.LANCZOS), (6, 6))
    else:   # two friends: the first a little behind on the left, the second in front on the right
        icon.alpha_composite(square(im, *boxes[0]).resize((100, 100), Image.LANCZOS), (4, 22))
        icon.alpha_composite(square(im, *boxes[1]).resize((100, 100), Image.LANCZOS), (56, 38))
    rim = icon.getchannel('A').point(lambda v: 255 if v > 40 else 0).filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.GaussianBlur(.8))
    out = Image.new('RGBA', (160, 160), (255, 255, 255, 0)); out.putalpha(rim)
    white = Image.new('RGBA', (160, 160), (255, 255, 255, 255)); white.putalpha(rim)
    white.alpha_composite(icon); white.save(f'assets/ui/icons-v2/{id}.png', optimize=True)
sheet = Image.open(D + 'ben-nora-cutout.webp').convert('RGBA')
save('ben', sheet.crop((0, 0, sheet.width // 2, sheet.height)), [(.57, .0, .5)])
save('nora', sheet.crop((sheet.width // 2, 0, sheet.width, sheet.height)), [(.5, .0, .57)])
mia = Image.open(D + 'mia-ollie-cutout.webp').convert('RGBA')
save('mia', mia, [(.33, -.01, .44), (.71, .05, .47)])
# the map pin shows the two friends as two faces (user request, PEOPLE.mia.faces): one icon each
save('mia-solo', mia, [(.71, .05, .47)], sprite=False)
save('ollie', mia, [(.33, -.01, .44)], sprite=False)

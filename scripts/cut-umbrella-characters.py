"""Umbrella case people from the two Higgsfield sheets (two per sheet, as the picnic case), background already removed
by Higgsfield (`*-cutout.webp`): Tess (left) and Ruby (right), Ella (left) and Finn (right), each sheet cut in half.
Same crop, size and face icon as scripts/cut-picnic-characters.py: a 3% margin, 700 px tall
-> assets/characters/<id>-higgsfield.png, and a 160 px face icon -> assets/ui/icons-v2/<id>.png.
The background remover took some light parts inside the drawings for the cream paper (Tess's sleeve, Ruby's tights,
Ella's muzzle, Finn's soles): everything inside a character's outline is made solid again from the original sheet.
Prints each sprite's size and the face viewBox for SPRITES. Run from the project folder: python -I scripts/cut-umbrella-characters.py"""
from PIL import Image, ImageFilter, ImageDraw, ImageChops
D = 'assets/characters/'
def trim(im):
    box = im.getchannel('A').point(lambda a: 255 if a > 24 else 0).getbbox()
    im = im.crop(box); m = round(max(im.size) * .03)
    out = Image.new('RGBA', (im.width + 2 * m, im.height + 2 * m)); out.paste(im, (m, m)); return out
def solid(cut, orig):
    a = cut.getchannel('A'); out = a.point(lambda v: 255 if v > 24 else 0); ImageDraw.floodfill(out, (0, 0), 128)
    inside = out.point(lambda v: 0 if v == 128 else 255).filter(ImageFilter.MinFilter(5))   # the soft outer edge stays
    weak = ImageChops.multiply(inside, a.point(lambda v: 255 if v < 250 else 0))
    cut.paste(orig.convert('RGBA'), (0, 0), weak); return cut
def square(im, cx, y0, side):
    face = Image.new('RGBA', (side, side)); face.paste(im.crop((round(cx - side / 2), y0, round(cx + side / 2), y0 + side)), (0, 0))
    return face
def save(id, im, head):
    """head: (centre x, top, side) as shares of the sprite's width/height"""
    im = trim(im); s = 700 / im.height
    im = im.resize((round(im.width * s), 700), Image.LANCZOS)
    im.save(D + f'{id}-higgsfield.png', optimize=True)
    W, H = im.size; x, y, z = head; cx, y0, side = round(x * W), round(y * H), round(z * H)
    print(id, im.size, f"face:'{round(cx - side / 2)} {y0} {side} {side}'")
    icon = Image.new('RGBA', (160, 160)); icon.paste(square(im, cx, y0, side).resize((148, 148), Image.LANCZOS), (6, 6))
    rim = icon.getchannel('A').point(lambda v: 255 if v > 40 else 0).filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.GaussianBlur(.8))
    white = Image.new('RGBA', (160, 160), (255, 255, 255, 255)); white.putalpha(rim)
    white.alpha_composite(icon); white.save(f'assets/ui/icons-v2/{id}.png', optimize=True)
for sheet, left, right in [('tess-ruby', ('tess', (.54, .0, .5)), ('ruby', (.39, .01, .53))),
                           ('ella-finn', ('ella', (.5, .02, .52)), ('finn', (.49, .0, .55)))]:
    im = solid(Image.open(D + f'{sheet}-cutout.webp').convert('RGBA'), Image.open(D + f'{sheet}-higgsfield-original.jpg'))
    save(left[0], im.crop((0, 0, im.width // 2, im.height)), left[1])
    save(right[0], im.crop((im.width // 2, 0, im.width, im.height)), right[1])

"""Cut the twin hit-and-run case's people (drawn before the story was handed over, user request) into sprites.

usage: python scripts/cut-twins-characters.py
  reads, all on flat magenta:
    assets/characters/twins-ada-short.png             Evan, Milo (legs shortened by scripts/shorten-twins-legs.py), Ada seated
    assets/characters/twins-iris-higgsfield-original.png   Iris is the third figure
    assets/characters/victor-bed-talk-higgsfield-original.png    Victor sitting up in bed (talking)
    assets/characters/victor-bed-lying-higgsfield-original.png   Victor lying back (not talking)
    assets/characters/ada-talk-higgsfield-original.png  Ada seated, stopped working, goggles up, looking at the player
  writes assets/characters/<evan|milo|ada|ada-talk|iris|victor-bed|victor-bed-lying>-higgsfield.png: magenta keyed out as in
  cut-christmas-talk.py, only the figure the seed point is on (no bits of a neighbour), trimmed with a 3% margin,
  700 px high. The two bed pictures are each cut to their own box (the bed is drawn the same size in both), so placing
  both at the same spot keeps the bed where it is when the sprite changes between them.
"""
from PIL import Image, ImageDraw, ImageFilter, ImageChops

A = 'assets/characters/'

def key_out(path):
    im = Image.open(A + path).convert('RGB')
    r, g, b = im.split()
    m = ImageChops.subtract(ImageChops.darker(r, b), g)            # how magenta a pixel is
    alpha = m.point(lambda v: 0 if v > 120 else (255 if v < 50 else int(255 * (120 - v) / 70)))
    # take the pink cast off the soft edges
    k = m.point(lambda v: min(255, max(0, v)) // 2)
    im = Image.merge('RGB', (ImageChops.subtract(r, k), g, ImageChops.subtract(b, k)))
    out = im.convert('RGBA'); out.putalpha(alpha); return out

def only(im, box, seed):
    """the figure under seed inside box, its alpha kept"""
    reg = im.crop(box); a = reg.getchannel('A')
    solid = a.point(lambda v: 255 if v > 127 else 0)
    ImageDraw.floodfill(solid, (seed[0] - box[0], seed[1] - box[1]), 128)
    keep = solid.point(lambda v: 255 if v == 128 else 0).filter(ImageFilter.MaxFilter(7))
    reg.putalpha(ImageChops.multiply(a, keep)); return reg

def trim(im, margin=.03, height=700, bbox=None):
    box = bbox or im.getchannel('A').point(lambda v: 255 if v > 40 else 0).getbbox()
    im = im.crop(box); m = int(max(im.size) * margin)
    out = Image.new('RGBA', (im.width + 2 * m, im.height + 2 * m), (0, 0, 0, 0)); out.paste(im, (m, m))
    return out.resize((round(out.width * height / out.height), height), Image.LANCZOS)

if __name__ == '__main__':
    twins = key_out('twins-ada-short.png'); iris = key_out('twins-iris-higgsfield-original.png')
    for name, src, box, seed in [('evan', twins, (0, 0, 500, 768), (270, 500)), ('milo', twins, (480, 0, 930, 768), (700, 500)),
                                 ('ada', twins, (930, 0, 1376, 768), (1060, 560)), ('iris', iris, (900, 0, 1376, 768), (1100, 500))]:
        fig = trim(only(src, box, seed)); fig.save(f'{A}{name}-higgsfield.png'); print(name, fig.size)
    fig = trim(only(key_out('ada-talk-higgsfield-original.png'), (0, 0, 1376, 768), (680, 450))); fig.save(f'{A}ada-talk-higgsfield.png'); print('ada-talk', fig.size)
    for name, s in [('victor-bed', 'talk'), ('victor-bed-lying', 'lying')]:
        fig = trim(only(key_out(f'victor-bed-{s}-higgsfield-original.png'), (0, 0, 1376, 768), (700, 560)))
        fig.save(f'{A}{name}-higgsfield.png'); print(name, fig.size)

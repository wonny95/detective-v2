"""Victor in his hospital bed seen straight from its foot, as the room is (the twins case, user request 2026-11-25: the bed
was drawn at an angle). Three Higgsfield pictures on magenta, the bed drawn at the same place in all:
assets/characters/victor-front-<talk|lying|mouth>-higgsfield-original.png (1792 x 2400, jobs 73a17b83, e1190674, 3fd86a3b).
Writes victor-front.png/.webp (awake), victor-front-lying.png/.webp (not talked to), both cut to the same box, 1000 px high,
and the mouths victor-front-closed/open (the open one only round the mouth). Prints the sizes and boxes for index.html.
Run from the project folder: python -I scripts/cut-victor-front.py"""
import importlib.util
from PIL import Image, ImageChops, ImageDraw, ImageFilter
spec = importlib.util.spec_from_file_location('cut', 'scripts/cut-twins-characters.py')
cut = importlib.util.module_from_spec(spec); spec.loader.exec_module(cut)
A, M, H = 'assets/characters/', 'assets/characters/mouths/', 1000
pic = {n: cut.only(cut.key_out(f'victor-front-{n}-higgsfield-original.png'), (0, 0, 1792, 2400), (900, 1100)) for n in ('talk', 'lying', 'mouth')}
boxes = [pic[n].getchannel('A').point(lambda v: 255 if v > 40 else 0).getbbox() for n in ('talk', 'lying')]
box = tuple(f(b[i] for b in boxes) for i, f in enumerate((min, min, max, max)))
out = {n: cut.trim(im, height=H, bbox=box) for n, im in pic.items()}
for n, name in (('talk', 'victor-front'), ('lying', 'victor-front-lying')):
    out[n].save(f'{A}{name}.png', optimize=True); out[n].save(f'{A}{name}.webp', quality=90)
m = int(max(box[2] - box[0], box[3] - box[1]) * .03); k = H / (box[3] - box[1] + 2 * m)
at = lambda x, y: (round((x - box[0] + m) * k), round((y - box[1] + m) * k))
x0, y0 = at(655, 452); x1, y1 = at(1165, 690)
mask = Image.new('L', out['talk'].size, 0); ImageDraw.Draw(mask).rectangle((x0 + 5, y0 + 5, x1 - 6, y1 - 6), fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(3))
hit = ImageChops.difference(out['talk'].convert('RGB'), out['mouth'].convert('RGB')).convert('L').point(lambda v: 255 if v > 34 else 0)
hit = hit.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(15)).filter(ImageFilter.GaussianBlur(2.5))
layer = out['mouth'].copy()
layer.putalpha(ImageChops.multiply(ImageChops.multiply(mask, hit), out['talk'].getchannel('A')))
for st, im in (('closed', out['talk']), ('open', layer)):
    im.crop((x0, y0, x1, y1)).save(f'{M}victor-front-{st}.png', optimize=True); im.crop((x0, y0, x1, y1)).save(f'{M}victor-front-{st}.webp', quality=92)
print('sprite', out['talk'].size, 'mouth', [x0, y0, x1 - x0, y1 - y0], 'face', at(600, 190), round(600 * k), 'foot', at(900, 2313), 'bed mid x', at(898, 0)[0] / out['talk'].width)

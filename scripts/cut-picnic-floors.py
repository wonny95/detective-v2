# Cuts the talk floors (ART_FLOOR) for the picnic case's five places (and the violin case's side passage) out of
# their Higgsfield outpaints.
# The outpaint (3:4, 1792x2400) holds the original picture somewhere across its full width; this finds its
# height by comparing a small copy at every offset, keeps everything below it, scales that strip to the
# original's width and saves assets/places/picnic-storyboard/<id>-floor.jpg. The outpaints are kept as
# <id>-outpaint-original.jpg. Run from the repo root: python -X utf8 -I scripts/cut-picnic-floors.py [ids]
import sys
from PIL import Image, ImageChops, ImageStat

DIR = 'assets/places/picnic-storyboard/'
PLACES = {   # place id: the picture the game draws (in DIR, or its own folder)
    'picnic': 'picnic-wide.png',
    'daycafe': 'cafe-day.png',
    'benhome': 'ben-home.png',
    'garden': 'garden.webp',
    'lobby': 'lobby-higgsfield.webp',
    'passage': 'assets/places/violin/passage.jpg',
}
# where the outpaint redrew the floor differently (the lobby's planks run the other way), the floor starts this
# many picture px higher and fades in over the picture's bottom: saved as <id>-floor.webp with alpha, and
# ART_FLOOR gets the same `overlap`
OVERLAP = {'lobby': 110, 'passage': 150}   # passage: the outpaint redrew the corridor (its walls and door elsewhere)
SMALL = 256   # search width

for pid in sys.argv[1:] or PLACES:
    src = PLACES[pid] if '/' in PLACES[pid] else DIR + PLACES[pid]
    DIR = src[:src.rindex('/') + 1]
    art = Image.open(src).convert('RGB')
    out = Image.open(f'{DIR}{pid}-outpaint-original.jpg').convert('RGB')
    w, h = art.size
    scale = out.width / w
    k = SMALL / out.width
    a = art.resize((SMALL, round(h * scale * k)), Image.LANCZOS)
    o = out.resize((SMALL, round(out.height * k)), Image.LANCZOS)
    diff = lambda y: sum(ImageStat.Stat(ImageChops.difference(o.crop((0, y, SMALL, y + a.height)), a)).mean)
    y = min(range(o.height - a.height + 1), key=diff)
    bottom = round((y + a.height) / k)
    lap = OVERLAP.get(pid, 0)
    floor = out.crop((0, bottom - round(lap * scale), out.width, out.height))
    fh = round(floor.height / scale)
    floor = floor.resize((w, fh), Image.LANCZOS)
    if lap:
        # alpha 0 → 1 (smoothstep) over the overlap, opaque below
        alpha = Image.new('L', (w, fh), 255)
        for row in range(lap):
            t = row / lap
            alpha.paste(round(255 * t * t * (3 - 2 * t)), (0, row, w, row + 1))
        floor.putalpha(alpha)
        floor.save(f'{DIR}{pid}-floor.webp', quality=90)
    else:
        # the outpaint redraws its copy of the picture a little lighter or darker: tint the floor's top to the
        # picture's bottom rows, fading out over FADE px, so the seam has no colour step
        edge = ImageStat.Stat(art.crop((0, h - 12, w, h))).mean
        top = ImageStat.Stat(floor.crop((0, 0, w, 12))).mean
        FADE = min(260, fh)
        px = floor.load()
        for row in range(FADE):
            t = 1 - row / FADE
            m = [1 + (e / max(f, 1) - 1) * t for e, f in zip(edge, top)]
            for x in range(w):
                r, g, b = px[x, row]
                px[x, row] = (min(255, round(r * m[0])), min(255, round(g * m[1])), min(255, round(b * m[2])))
        floor.save(f'{DIR}{pid}-floor.jpg', quality=90)
    print(pid, 'picture ends at y', bottom, 'of', out.height, '(match', round(diff(y), 1), ') -> floor', w, 'x', fh, 'overlap', lap)

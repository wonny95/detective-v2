"""Talking mouths for the Valentine case (user request 2026-11-27): Penny and Suzy, front view and mood.

The character sheets (scripts/cut-valentine-characters.py) carry round patches of each face, drawn at the front view's
angle: closed and open for the front view, open only for the moods (penny-worried, suzy-sorry). The patch is found on
the sprite by matching its eyes and nose (the mouth left out) over sizes and places, Pillow only; the mouth area is
where the closed and open patches differ (the moods take the front view's area, in the same place under the nose).
closed = the sprite as drawn there; open = the patch's open mouth laid over it with a soft oval edge.
Writes assets/characters/mouths/<name>-closed|open.png/.webp and prints the MOUTHS lines.
Run from the project folder: python -I scripts/make-valentine-mouths.py"""
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageStat

C = 'assets/characters/'; M = C + 'mouths/'
# name: (sprite, its face box, open patch, closed patch or the name whose mouth area it takes)
P = {
    'penny': ('penny-higgsfield', (92, 40, 392, 340), 'penny-patch-open', 'penny-patch-closed'),
    'suzy': ('suzy-higgsfield', (25, 70, 325, 370), 'suzy-patch-open', 'suzy-patch-closed'),
    'penny-worried': ('penny-worried', (83, 40, 383, 340), 'penny-worried-patch-open', 'penny'),
    'suzy-sorry': ('suzy-sorry', (17, 70, 317, 370), 'suzy-sorry-patch-open', 'suzy'),
}
Q = 4   # matching works on a quarter-size grey copy


def grey(im, bg=(255, 255, 255)):
    flat = Image.new('RGB', im.size, bg); flat.paste(im, (0, 0), im)
    return flat.convert('L')


def mouth_area(closed, opened):
    """the open patch's mouth box (patch px): where it differs from a closed face once the two are laid one on the
    other (the patches are a pixel or two apart in size and place)"""
    a, b = grey(opened), grey(closed)
    w, h = a.size
    win = (int(w * .15), int(h * .15), int(w * .85), int(h * .6))   # eyes and nose
    best = min(((ImageStat.Stat(ImageChops.difference(a.crop(win), b.crop((win[0] + dx, win[1] + dy, win[2] + dx, win[3] + dy)))).mean[0], dx, dy)
                for dx in range(-10, 11, 2) for dy in range(-10, 11, 2)))
    _, dx, dy = best
    shifted = Image.new('L', a.size, 255); shifted.paste(b, (-dx, -dy))
    d = ImageChops.difference(a, shifted).point(lambda v: 255 if v > 50 else 0)
    w, h = d.size   # only the lower middle of the face (the round edges of the two patches differ a little too)
    keep = Image.new('L', d.size); ImageDraw.Draw(keep).rectangle((int(w * .33), int(h * .6), int(w * .67), int(h * .9)), fill=255)
    d = ImageChops.multiply(d, keep).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(9))
    return d.getbbox()


def open_mouth(opened):
    """the open mouth's box (patch px): the dark inside of the mouth under the nose, grown to take in the lips
    (the closed and open patches differ a little everywhere in their brush strokes, so a difference finds too much)"""
    g = grey(opened); w, h = g.size
    win = (int(w * .33), int(h * .67), int(w * .67), int(h * .92))
    dark = g.crop(win).point(lambda v: 255 if v < 120 else 0).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(3))
    # only the piece joined to the middle (the mouth), not the chin line, nose or glasses at the window's edges
    cx, px = dark.width // 2, dark.load()
    seed = next((cx + dx, y) for y in range(dark.height // 5, dark.height) for dx in (0, -6, 6, -12, 12) if px[cx + dx, y] == 255)
    ImageDraw.floodfill(dark, seed, 128)
    x0, y0, x1, y1 = dark.point(lambda v: 255 if v == 128 else 0).getbbox()
    x0, y0, x1, y1 = x0 + win[0], y0 + win[1], x1 + win[0], y1 + win[1]
    gx, gy = (x1 - x0) * .25 + 6, (y1 - y0) * .3 + 6
    return (round(x0 - gx), round(y0 - gy), round(x1 + gx), round(y1 + gy))


def find(sprite, face, patch, mouth):
    """the patch's scale and corner on the sprite, from its eyes and nose (everything above the mouth)"""
    w, h = patch.size
    top = (int(w * .18), int(h * .2), int(w * .82), mouth[1] - 4)   # eyes, glasses, nose
    tmpl_full = grey(patch.crop(top))
    area = grey(sprite.crop(face)); area = area.resize((area.width // Q, area.height // Q))
    best = None
    for k in range(40, 76):
        s = k / 100   # patch px -> sprite px
        tw, th = round(tmpl_full.width * s / Q), round(tmpl_full.height * s / Q)
        if tw < 8 or th < 6 or tw >= area.width or th >= area.height: continue
        t = tmpl_full.resize((tw, th))
        for y in range(0, area.height - th):
            for x in range(0, area.width - tw):
                v = ImageStat.Stat(ImageChops.difference(area.crop((x, y, x + tw, y + th)), t)).mean[0]
                if best is None or v < best[0]: best = (v, s, x, y)
    v, s, x, y = best
    # back to the patch's own corner, in sprite px
    return s, face[0] + x * Q - top[0] * s, face[1] + y * Q - top[1] * s, v


areas = {}
# the drawn mouth's middle on the sprite (sprite px), where the matching on eyes and nose went wrong
AT = {'penny-worried': (301, 272)}
for name, (spr, face, po, pc) in P.items():
    sprite = Image.open(C + spr + '.webp').convert('RGBA')
    opened = Image.open(M + po + '.png').convert('RGBA')
    mouth = open_mouth(opened)
    print(name, 'mouth in patch', mouth)
    s, px, py, err = find(sprite, face, opened, mouth)
    if name in AT:   # the match slid off (worried Penny's hand and spines): put the mouth's middle on the drawn one
        (cx, cy), mcx, mcy = AT[name], (mouth[0] + mouth[2]) / 2, (mouth[1] + mouth[3]) / 2
        px, py = cx - mcx * s, cy - mcy * s
    # the mouth's box on the sprite, a little bigger, and the open patch laid over it in an oval
    mx0, my0, mx1, my1 = mouth
    pad = .18
    bw, bh = (mx1 - mx0) * s, (my1 - my0) * s
    x0 = round(px + mx0 * s - bw * pad); y0 = round(py + my0 * s - bh * pad)
    x1 = round(px + mx1 * s + bw * pad); y1 = round(py + my1 * s + bh * pad)
    big = opened.resize((round(opened.width * s), round(opened.height * s)), Image.LANCZOS)
    lay = Image.new('RGBA', sprite.size); lay.paste(big, (round(px), round(py)))
    mask = Image.new('L', sprite.size); ImageDraw.Draw(mask).ellipse((x0 + 2, y0 + 2, x1 - 2, y1 - 2), fill=255)
    mask = ImageChops.multiply(mask.filter(ImageFilter.GaussianBlur(3)), lay.getchannel('A'))
    o = sprite.copy(); o.paste(lay, (0, 0), mask)
    box = (x0, y0, x1, y1)
    for st, im in (('closed', sprite.crop(box)), ('open', o.crop(box))):
        im.save(M + f'{name}-{st}.png', optimize=True); im.save(M + f'{name}-{st}.webp', quality=92, method=6)
    w, h = x1 - x0, y1 - y0
    key = name.replace('-', ':', 1)
    print(f"  {key if ':' not in key else repr(key)}:{{closed:[{x0},{y0},{w},{h}], open:[{x0},{y0},{w},{h}]}},   // scale {s:.2f}, match {err:.1f}")

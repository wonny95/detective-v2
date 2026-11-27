"""Valentine case: the chocolates in 소지품 as loose pieces, one picture for each count (user decision 2026-11-27: how
many flowers are short changes with each new game, 1-3; the bag pictures from the sheet show three, so 소지품 shows the
pieces themselves instead). Made from the cut pieces (choc-pink-heart.webp, choc-flower.webp, scripts/cut-valentine-props.py),
nothing drawn over them: pile-<kind>-<n>.webp, 300x240, transparent.
Run from the project folder: python -I scripts/make-valentine-piles.py   (Pillow only)"""
from PIL import Image

P = 'assets/places/valentine/'
W, H, SIZE = 300, 240, 150
# where each piece's middle is and how it is turned (the top one of three is pasted first, behind the other two)
SPOTS = {1: [(150, 125, -6)], 2: [(103, 135, -12), (197, 122, 10)], 3: [(150, 82, 3), (94, 158, -10), (206, 152, 9)]}

for kind, src in (('pink-hearts', 'choc-pink-heart'), ('flowers', 'choc-flower')):
    piece = Image.open(P + src + '.webp').convert('RGBA')
    sc = SIZE / max(piece.size)
    piece = piece.resize((round(piece.width * sc), round(piece.height * sc)), Image.LANCZOS)
    for n, spots in SPOTS.items():
        im = Image.new('RGBA', (W, H))
        for x, y, rot in spots:
            p = piece.rotate(rot, Image.BICUBIC, expand=True)
            im.alpha_composite(p, (round(x - p.width / 2), round(y - p.height / 2)))
        im.save(P + f'pile-{kind}-{n}.webp', quality=90)
        print(kind, n, im.getbbox())

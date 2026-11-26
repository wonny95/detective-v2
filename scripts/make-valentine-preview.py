"""Valentine case: Penny and Suzy stood on their backgrounds, for the design doc (user request 2026-11-26).

Not game art. Puts the cut figures (scripts/cut-valentine-characters.py) on the 3:4 originals at a trial place and size:
Penny in front of the classroom desk, Suzy on the floor left of the shop counter. Each picture shows the idle pose
(`:work`, before the detective talks) and the front view (talk) side by side.
Writes design/valentine-preview/classroom-penny.jpg, shop-suzy.jpg.
Run from the project folder: python -I scripts/make-valentine-preview.py   (Pillow only)"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

C, P, OUT = 'assets/characters/', 'assets/places/valentine/', Path('design/valentine-preview')
OUT.mkdir(exist_ok=True)
# (background, character, feet centre x, feet y, figure height) on the 1792x2400 originals
SCENES = {
    'classroom-penny': (P + 'classroom-higgsfield-original.png', 'penny', 820, 1930, 720),
    'shop-suzy': (P + 'shop-v2-higgsfield-original.png', 'suzy', 390, 1900, 820),
}
W = 600   # each panel's width


def panel(bg, fig_path, fx, fy, fh, label):
    im = Image.open(bg).convert('RGBA')
    fig = Image.open(fig_path).convert('RGBA')
    fig = fig.resize((round(fig.width * fh / fig.height), fh), Image.LANCZOS)
    im.alpha_composite(fig, (fx - fig.width // 2, fy - fh))
    im = im.convert('RGB').resize((W, round(im.height * W / im.width)), Image.LANCZOS)
    d = ImageDraw.Draw(im)
    try:
        font = ImageFont.truetype('C:/Windows/Fonts/malgunbd.ttf', 26)
    except OSError:
        font = ImageFont.load_default()
    d.rounded_rectangle((14, 14, 30 + d.textlength(label, font=font), 56), 10, fill=(255, 250, 240))
    d.text((22, 18), label, font=font, fill=(90, 60, 40))
    return im


for name, (bg, cid, fx, fy, fh) in SCENES.items():
    a = panel(bg, f'{C}{cid}-work.webp', fx, fy, fh, '평소 자세')
    b = panel(bg, f'{C}{cid}-higgsfield.webp', fx, fy, fh, '말을 걸면(정면)')
    sheet = Image.new('RGB', (W * 2 + 16, a.height), (255, 255, 255))
    sheet.paste(a, (0, 0)); sheet.paste(b, (W + 16, 0))
    sheet.save(OUT / f'{name}.jpg', quality=86)
    print(OUT / f'{name}.jpg', sheet.size)

"""160 px face icons for the twins case's people (Iris, Victor, Ada), cut from their talk sprites with the same white rim as
the other cases' icons (scripts/make-christmas-face-icons.py). They were missing: the discovery notice showed the pending
silhouette (user report 2026-11-25). Victor is cut out of his bed (BED: his outline).
usage: python -I scripts/make-twins-face-icons.py
"""
from PIL import Image, ImageChops, ImageDraw, ImageFilter

FACES = {   # id: (sprite, face box x y side)
    'iris': ('iris-higgsfield.png', (64, 8, 270)),
    'victor': ('victor-front.png', (236, 19, 268)),
    'ada': ('ada-talk-higgsfield.png', (55, 5, 290)),
}
BED = [(289.25, 65.5), (285, 82.5), (284, 90.5), (275, 98.75), (261.5, 114.5), (257.5, 135), (257.75, 143.75), (261.5, 161.25), (272.5,
       180.5), (294.5, 203.75), (295, 212.5), (285, 217), (260, 230), (240, 252), (224.5, 280), (212.5, 315), (208, 340), (542.5, 340),
       (533.75, 315), (518.75, 280), (498, 240), (476.25, 223), (461.25, 215.5), (477.5, 219.25), (491.5, 217), (490.5, 209.5), (467, 202.5),
       (499, 180.5), (480, 178.75), (465.5, 186.25), (475, 171.25), (482, 152.5), (484.5, 135), (477.5, 113), (460, 92), (457.5, 81.25),
       (454.25, 65.5), (454.25, 0), (285, 0)]
for id, (src, (x, y, side)) in FACES.items():
    im = Image.open('assets/characters/' + src).convert('RGBA')
    if id == 'victor':   # in his bed: him alone, the rails and the pillow left out (BED)
        m = Image.new('L', (im.width * 4, im.height * 4)); ImageDraw.Draw(m).polygon([(px * 4, py * 4) for px, py in BED], fill=255)
        im.putalpha(ImageChops.multiply(im.getchannel('A'), m.resize(im.size, Image.LANCZOS)))
    face = Image.new('RGBA', (side, side)); face.paste(im.crop((x, y, x + side, y + side)), (0, 0))
    if id == 'ada':   # a bit of her tail at the side
        ImageDraw.Draw(face).polygon([(268, 170), (262, 195), (252, 210), (243, 224), (240, 260), (239, 290), (290, 290), (290, 170)], fill=(0, 0, 0, 0))
    icon = Image.new('RGBA', (160, 160)); icon.paste(face.resize((148, 148), Image.LANCZOS), (6, 6))
    rim = icon.getchannel('A').point(lambda v: 255 if v > 40 else 0).filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.GaussianBlur(.8))
    white = Image.new('RGBA', (160, 160), (255, 255, 255, 255)); white.putalpha(rim)
    white.alpha_composite(icon); white.save(f'assets/ui/icons-v2/{id}.png', optimize=True); white.save(f'assets/ui/icons-v2/{id}.webp', quality=90)
    print(id)

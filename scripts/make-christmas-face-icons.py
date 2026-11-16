"""160 px face icons for the Christmas star case's people (Daisy = id holly, May = mae, Nico), cut from their talk
sprites with the same boxes as SPRITES[id].face and the same white rim as the other cases' icons
(scripts/cut-violin-characters.py). They were missing: the discovery notice showed the pending silhouette (user report).
usage: python scripts/make-christmas-face-icons.py
"""
from PIL import Image, ImageFilter

FACES = {   # id: (sprite, face box x y side) as in index.html SPRITES
    'holly': ('assets/characters/holly-talk.png', (40, 0, 360)),
    'mae': ('assets/characters/mae-talk.png', (38, 0, 372)),
    'nico': ('assets/characters/nico-higgsfield.png', (60, 0, 357)),
}
for id, (src, (x, y, side)) in FACES.items():
    im = Image.open(src).convert('RGBA')
    face = Image.new('RGBA', (side, side)); face.paste(im.crop((x, y, x + side, y + side)), (0, 0))
    icon = Image.new('RGBA', (160, 160)); icon.paste(face.resize((148, 148), Image.LANCZOS), (6, 6))
    rim = icon.getchannel('A').point(lambda v: 255 if v > 40 else 0).filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.GaussianBlur(.8))
    white = Image.new('RGBA', (160, 160), (255, 255, 255, 255)); white.putalpha(rim)
    white.alpha_composite(icon); white.save(f'assets/ui/icons-v2/{id}.png', optimize=True)
    print(id)

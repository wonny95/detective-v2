"""Umbrella case places, each drawn as one tall Higgsfield picture with its floor (as Betty's home): scaled to 1376 wide,
a 1376x768 band from `top` is the place picture (<id>.webp), everything under it the conversation floor (<id>-floor.jpg,
ART_FLOOR). The band starts a little down where the drawing's ceiling or sky is empty, so the hall's banner on the floor
stays inside the picture. Also the toy bazaar photo pinned on the hall's board (bazaar-photo.webp, drawn into ART.hall
at full size so the evidence photo is sharp) and the front of the hall's umbrella stand (stand-front.png), laid over the
umbrella put in it, so the umbrella goes into the stand.
Run from the project folder: python -I scripts/cut-umbrella-places.py"""
from PIL import Image
D = 'assets/places/umbrella/'
TOP = {'hall': 100, 'toynest': 60, 'windmill': 50}
for id, top in TOP.items():
    im = Image.open(D + f'{id}-higgsfield-original.jpg').convert('RGB').resize((1376, 1843), Image.LANCZOS)
    im.crop((0, top, 1376, top + 768)).save(D + f'{id}.webp', quality=88)
    floor = im.crop((0, top + 768, 1376, 1843)); floor.save(D + f'{id}-floor.jpg', quality=85)
    print(id, 'floor h', floor.height)
    if id == 'hall':   # the stand under its rim (picture px)
        im.crop((204, top + 517, 304, top + 690)).save(D + 'stand-front.png', optimize=True)
Image.open(D + 'bazaar-photo-higgsfield-original.jpg').convert('RGB').resize((720, 538), Image.LANCZOS).save(D + 'bazaar-photo.webp', quality=88)

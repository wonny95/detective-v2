"""Umbrella case places, each drawn as one tall Higgsfield picture with its floor (as Betty's home): scaled to 1376 wide,
a 1376x768 band from `top` is the place picture (<id>.webp), everything under it the conversation floor (<id>-floor.jpg,
ART_FLOOR). The band starts a little down where the drawing's ceiling or sky is empty.
The hall is the redrawn picture (2026-11-18, user pick A: no floor banner, no umbrella stand, a potted plant by the door,
a board and a poster with no readable words); the first hall (hall-higgsfield-original.jpg), its umbrella stand front
(stand-front.png) and the bazaar photo (bazaar-photo.webp) are kept on disk but no longer cut or used.
Toy Nest and Windmill Hill left the case (everyone in the hall) and are not cut again.
Run from the project folder: python -I scripts/cut-umbrella-places.py"""
from PIL import Image
D = 'assets/places/umbrella/'
SRC = {'hall': 'hall-v2-a-higgsfield-original.png'}
TOP = {'hall': 100}
for id, top in TOP.items():
    im = Image.open(D + SRC[id]).convert('RGB').resize((1376, 1843), Image.LANCZOS)
    im.crop((0, top, 1376, top + 768)).save(D + f'{id}.webp', quality=88)
    floor = im.crop((0, top + 768, 1376, 1843)); floor.save(D + f'{id}-floor.jpg', quality=85)
    print(id, 'floor h', floor.height)

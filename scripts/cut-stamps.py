# The status stamps out of assets/ui/stamps-higgsfield-original.png (Higgsfield nano_banana_2_1 16:9 2K,
# job d2b4be43-ab70-4031-ba89-b96814c3ec72, 12 rubber stamps on plain white). White becomes see-through: each pixel's
# alpha is how far it is from white, and its colour is un-mixed from the white so the worn ink edges stay soft.
# Only MISSION CLEAR is used (the solved case's stamp, in red); the other eleven were tried in a mockup and removed
# (user decision 2026-11-26). Writes assets/ui/stamps/mission-clear-red.webp.
import os
from PIL import Image
D = 'assets/ui/'
S = Image.open(D + 'stamps-higgsfield-original.png').convert('RGB')
os.makedirs(D + 'stamps', exist_ok=True)
# boxes on the half-size view (1376 x 768), doubled for the 2752 x 1536 sheet
BOXES = {
  'mission-accepted': (50, 30, 280, 255), 'mission-complete': (310, 65, 690, 215), 'case-closed': (705, 85, 1030, 200),
  'solved': (1065, 90, 1340, 220), 'new-case': (25, 280, 300, 495), 'in-progress': (350, 330, 660, 442),
  'investigating': (750, 270, 980, 500), 'top-secret': (1055, 325, 1350, 445), 'mission-clear': (50, 520, 280, 745),
  'approved': (400, 515, 610, 745), 'case-file': (720, 530, 1015, 740), 'complete': (1065, 525, 1345, 745)}
for name, b in BOXES.items():
    if name != 'mission-clear': continue
    i = S.crop(tuple(v * 2 for v in b)).convert('RGBA'); p = i.load()
    for y in range(i.height):
        for x in range(i.width):
            r, g, bl, _ = p[x, y]
            a = (255 - min(r, g, bl)) / 255
            a = max(0, min(1, (a - .06) / .8))
            if a <= 0: p[x, y] = (0, 0, 0, 0); continue
            c = [max(0, min(255, round((v - (1 - a) * 255) / a))) for v in (r, g, bl)]
            p[x, y] = (*c, round(a * 255))
    i = i.crop(i.getchannel('A').point(lambda v: 255 if v > 30 else 0).getbbox())
    i.thumbnail((360, 360), Image.LANCZOS)
    blue = i
# MISSION CLEAR in red as well (user request 2026-11-26: the solved case's stamp, red like SOLVED was): the same ink
# shape, its colour moved onto the game's stamp red (#B8323A), lighter where the blue was lighter
b = blue.convert('RGBA'); p = b.load()
for y in range(b.height):
    for x in range(b.width):
        r, g, bl, a = p[x, y]
        if not a: continue
        k = max(0, min(1, (r + g + bl) / 3 / 255 - .1))   # 0 dark ink .. 1 light
        p[x, y] = (round(184 + (235 - 184) * k), round(50 + (120 - 50) * k), round(58 + (125 - 58) * k), a)
b.save(f'{D}stamps/mission-clear-red.webp', quality=90, method=6); print('mission-clear-red', b.size)

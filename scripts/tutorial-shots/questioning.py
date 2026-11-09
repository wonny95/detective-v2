# 7 심문해요: cut from the tutorial's own moving questioning page (TUT_DEMO in index.html: a made-up claim, the lamp photo
# picked, the questioning room behind), not from the game: the game's own questioning shows the culprit.
# usage: node scripts/tutorial-shots/questioning.mjs scripts/tutorial-shots/shots/m-int.png
#        python scripts/tutorial-shots/questioning.py scripts/tutorial-shots/shots
import json, sys
from PIL import Image, ImageDraw, ImageOps
S = sys.argv[1]
W, H, PAD = 900, 720, 20
BG, INK = (243, 236, 221), (74, 54, 40)
title, x0, y0, x1, y1 = json.load(open(S + '/m-int.png.json', encoding='utf-8'))
assert title == '심문해요', title
im = Image.open(S + '/m-int.png').convert('RGB').crop((round(x0 * 3) + 6, round(y0 * 3) + 6, round(x1 * 3) - 6, round(y1 * 3) - 6))
im = ImageOps.fit(im, (W - 2 * PAD, H - 2 * PAD), Image.LANCZOS)
c = Image.new('RGB', (W, H), BG)
mask = Image.new('L', im.size, 0)
ImageDraw.Draw(mask).rounded_rectangle((0, 0, im.size[0] - 1, im.size[1] - 1), 22, fill=255)
c.paste(im, (PAD, PAD), mask)
ImageDraw.Draw(c).rounded_rectangle((PAD, PAD, PAD + im.size[0] - 1, PAD + im.size[1] - 1), 22, outline=INK, width=4)
c.save('assets/ui/tutorial/tut-7.webp', quality=86)
print(c.size)

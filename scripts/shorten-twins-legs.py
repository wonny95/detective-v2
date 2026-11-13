"""The twin meerkats (Evan, Milo) came out long-legged from Higgsfield however it was asked; squash their trouser band so
they have the short legs of the other characters (user: they suddenly had long legs). Free, no regeneration.

usage: python scripts/shorten-twins-legs.py
  reads assets/characters/twins-ada-higgsfield-original.png (twins left, Ada seated right, magenta), writes
  assets/characters/twins-ada-short.png: in the twins' columns (x 0-930) the band y 545-720 (knees to ankles) is
  scaled to 55% of its height and everything above it moves down, so the feet stay on the same baseline.
"""
from PIL import Image
im = Image.open('assets/characters/twins-ada-higgsfield-original.png').convert('RGB'); W, H = im.size
x0, x1, y0, y1, k = 0, 930, 545, 720, 0.55
left = im.crop((x0, 0, x1, H))
band = left.crop((0, y0, x1 - x0, y1)).resize((x1 - x0, int((y1 - y0) * k)), Image.LANCZOS)
shift = (y1 - y0) - band.height
new = Image.new('RGB', (x1 - x0, H), im.getpixel((5, 5)))
new.paste(left.crop((0, 0, x1 - x0, y0)), (0, shift)); new.paste(band, (0, shift + y0))
new.paste(left.crop((0, y1, x1 - x0, H)), (0, shift + y0 + band.height))
out = im.copy(); out.paste(new, (x0, 0)); out.save('assets/characters/twins-ada-short.png')
print('twins-ada-short.png', out.size)

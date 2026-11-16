"""Christmas case: the backdrop of the scale close look 'weigh' (user request 2026-11-16: a simple Christmas pattern instead
of the blurred sleigh, not clashing with the scale's silver/gold or the boxes' red/gold).
weigh-pattern.jpg: weigh-pattern-higgsfield-original.png (pine green, cream snowflakes and stars, sage holly, motifs kept
off the edges) made to repeat without a seam: each edge band is cross-faded with the band at the opposite edge and that
opposite band cut off. Scaled to 640 square. Run from the project folder."""
from PIL import Image

D = 'assets/places/christmas/'
B = 48   # band; no motif lies within it at the right or bottom edge
im = Image.open(D + 'weigh-pattern-higgsfield-original.png').convert('RGB')

def seam(img):
    W, H = img.size
    out = img.crop((0, 0, W - B, H))
    for x in range(B):
        t = x / B
        col = Image.blend(img.crop((W - B + x, 0, W - B + x + 1, H)), img.crop((x, 0, x + 1, H)), t)
        out.paste(col, (x, 0))
    return out

im = seam(im)                                                         # left-right
im = seam(im.transpose(Image.Transpose.TRANSPOSE)).transpose(Image.Transpose.TRANSPOSE)   # top-bottom
im.resize((640, 640), Image.LANCZOS).save(D + 'weigh-pattern.jpg', quality=88)
print(im.size)

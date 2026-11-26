# The umbrella case's cover (user request 2026-11-26): Ella holding out the star umbrella in the lost and found hall,
# close on her upper body and the umbrella (user request: not her whole body). Both pictures as made
# (assets/characters/ella-give.webp over assets/places/umbrella/hall.webp, the hall grown to match), cut to the list
# photo's ratio (1.42) from her ears down to just under the umbrella.
from PIL import Image
E = Image.open('assets/characters/ella-give.webp').convert('RGBA')
es = 1.1; E = E.resize((round(E.width * es), round(E.height * es)), Image.LANCZOS)
H = Image.open('assets/places/umbrella/hall.webp').convert('RGBA')
hs = 1.18; H = H.resize((round(H.width * hs), round(H.height * hs)), Image.LANCZOS)
cx = H.width // 2 + round(40 * hs)          # where she stood on the full-body cover
ex, ey = cx - E.width // 2, H.height - E.height - round(34 * hs)
H.alpha_composite(E, (ex, ey))
W, Ht = 800, round(800 / 1.42)
x0, y0 = cx - W // 2, ey + 6
H.crop((x0, y0, x0 + W, y0 + Ht)).convert('RGB').save('assets/places/umbrella/ella-cover.webp', quality=88, method=6)
print(W, Ht)

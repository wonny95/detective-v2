"""Review 10 of the Christmas case: the back of Tess's toy star no longer peels (that clue left the story). Cuts the
Higgsfield edit (assets/places/christmas/toy-star-back-fix-higgsfield-original.png, on magenta) into toy-star-back.png
at the old picture's size, so the close look's frame stays. Run from the project folder."""
from PIL import Image
src = Image.open('assets/places/christmas/toy-star-back-fix-higgsfield-original.png').convert('RGB')
W, H = src.size
out = Image.new('RGBA', src.size); s, d = src.load(), out.load()
for y in range(H):
    for x in range(W):
        r, g, b = s[x, y]
        k = min(r, b) - g
        a = 1.0 if k < 60 else 0.0 if k > 170 else (170 - k) / 110
        if a <= 0: d[x, y] = (0, 0, 0, 0); continue
        if a < 1: r = (r - (1 - a) * 255) / a; b = (b - (1 - a) * 255) / a
        m = min(r, b)
        if m > g: r -= m - g; b -= m - g
        d[x, y] = (max(0, min(255, round(r))), g, max(0, min(255, round(b))), round(a * 255))
out = out.crop(out.getchannel('A').point(lambda v: 255 if v > 48 else 0).getbbox())
out.resize((601, 577), Image.LANCZOS).save('assets/places/christmas/toy-star-back.png')
print(out.size)

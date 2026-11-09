# The tutorial pictures: crops of real game screens (390x844 CSS px, shot at 3x), on the tutorial's paper.
import os
from PIL import Image, ImageDraw, ImageOps
SH = 'scripts/tutorial-shots/shots/'
OUT = 'assets/ui/tutorial/'
os.makedirs(OUT, exist_ok=True)
W, H, PAD, GAP = 900, 720, 20, 40
BG, INK = (243, 236, 221), (74, 54, 40)

def crop(name, x0, y0, x1, y1, size):
    im = Image.open(SH + name + '.png').convert('RGB').crop((x0 * 3, y0 * 3, x1 * 3, y1 * 3))
    return ImageOps.fit(im, size, Image.LANCZOS)

def panel(canvas, im, x, y, r=22):
    mask = Image.new('L', im.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, im.size[0] - 1, im.size[1] - 1), r, fill=255)
    canvas.paste(im, (x, y), mask)
    ImageDraw.Draw(canvas).rounded_rectangle((x, y, x + im.size[0] - 1, y + im.size[1] - 1), r, outline=INK, width=4)

def arrow(canvas, cx, cy):
    d = ImageDraw.Draw(canvas)
    d.line((cx - 13, cy, cx + 11, cy), fill=INK, width=6)
    d.line((cx + 1, cy - 11, cx + 13, cy), fill=INK, width=6)
    d.line((cx + 1, cy + 11, cx + 13, cy), fill=INK, width=6)

def two(name, a, b):
    pw = (W - 2 * PAD - GAP) // 2
    c = Image.new('RGB', (W, H), BG)
    panel(c, crop(*a, (pw, H - 2 * PAD)), PAD, PAD)
    panel(c, crop(*b, (pw, H - 2 * PAD)), PAD + pw + GAP, PAD)
    arrow(c, W // 2, H // 2)
    c.save(OUT + name, quality=86)

def one(name, a):
    c = Image.new('RGB', (W, H), BG)
    panel(c, crop(*a, (W - 2 * PAD, H - 2 * PAD)), PAD, PAD)
    c.save(OUT + name, quality=86)

# 1 질문하고 들어요: the question under the person → the note up, the answer playing (no answer written)
two('tut-1.webp', ('a-talk', 10, 166, 380, 780), ('b-note', 14, 50, 376, 650))
# 2 빈칸을 채워요: the blanks and the word cards
one('tut-2.webp', ('b-note', 24, 418, 366, 690))
# 3 기록 완료로 확인해요: wrong blanks after a check (the cards left, which would tell the answers, are cut off)
one('tut-3.webp', ('c-wrong', 24, 340, 366, 612))
# 4 현장을 조사해요: the first map → the place
two('tut-4.webp', ('j-map', 0, 140, 262, 574), ('h-place2', 26, 92, 300, 546))
# 5 Note를 펼쳐 봐요: the tabs, the person, 📌 (cut above the answers)
one('tut-5.webp', ('k-person', 10, 36, 366, 318))
# 6 추리해요: the deduction board's first question, the suspects not yet known (7 심문해요 is questioning.py)
one('tut-6.webp', ('i-deduce', 0, 40, 390, 348))
print(sorted(os.listdir(OUT)), [os.path.getsize(OUT + f) // 1024 for f in sorted(os.listdir(OUT))])

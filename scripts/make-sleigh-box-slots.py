"""Christmas case: the sleigh keeps its own five boxes (sleigh.jpg; user report 2026-11-16: boxes drawn over an empty sleigh
looked unnatural). Only a box being opened is taken away: its place filled from the empty sleigh (gap), the open box
drawn there, then what stands in front of it again (the boxes in front, the left wall, the front rail).
- box-gap-<k>.png: sleigh-empty.jpg inside box k's outline, less the outlines of the boxes in front of it
- box-cut-<k>.png: box k cut out of sleigh.jpg (only those that stand in front of another box)
- sleigh-front.png: the left wall and the front rail cut out of sleigh.jpg
Prints each piece's place for index.html (XMAS_SLOTS). Run from the project folder after scripts/make-sleigh-boxes.py."""
import json
from PIL import Image, ImageDraw, ImageFilter, ImageChops

D = 'assets/places/christmas/'
sl = Image.open(D + 'sleigh.jpg').convert('RGBA')
empty = Image.open(D + 'sleigh-empty.jpg').convert('RGBA')
# each box's outline, bow included (sleigh.jpg pixels)
BOX = [
    [(428, 422), (460, 409), (466, 389), (548, 389), (552, 412), (584, 424), (584, 550), (428, 550)],
    [(524, 466), (554, 453), (558, 433), (650, 433), (653, 455), (682, 464), (682, 564), (600, 604), (524, 582)],
    [(634, 530), (666, 519), (670, 500), (748, 500), (751, 519), (789, 531), (789, 632), (705, 675), (634, 642)],
    [(760, 494), (788, 485), (796, 466), (884, 466), (889, 485), (915, 494), (915, 604), (830, 634), (760, 607)],
    [(876, 522), (904, 511), (910, 491), (988, 491), (993, 511), (1044, 521), (1044, 604), (876, 604)],
]
FRONT = {0: [1], 1: [2], 2: [], 3: [2], 4: [3]}   # the boxes standing in front of each one (drawn later)
LEFT_WALL = [(410, 486), (440, 492), (466, 508), (486, 530), (500, 558), (512, 598), (522, 640), (532, 700), (410, 700)]
RAIL = [(836, 652), (842, 622), (852, 604), (872, 594), (900, 590), (960, 574), (1020, 556), (1080, 536), (1110, 526),
        (1110, 720), (800, 720), (812, 690), (826, 668)]

def poly(points, grow=0):
    m = Image.new('L', sl.size); ImageDraw.Draw(m).polygon(points, fill=255)
    return m.filter(ImageFilter.MaxFilter(grow * 2 + 1)) if grow else m

def save(img, mask, name):
    out = img.copy(); out.putalpha(mask)
    box = mask.getbbox(); out.crop(box).save(D + name)
    return [box[0], box[1], box[2] - box[0], box[3] - box[1]]

slots = []
for k, pts in enumerate(BOX):
    gap = poly(pts, 3)
    for j in FRONT[k]: gap = ImageChops.subtract(gap, poly(BOX[j]))
    g = save(empty, gap, f'box-gap-{k}.png')
    cut = save(sl, poly(pts), f'box-cut-{k}.png') if any(k in f for f in FRONT.values()) else None
    slots.append({ 'gap':g, 'cut':cut, 'front':FRONT[k] })
front = ImageChops.lighter(poly(LEFT_WALL), poly(RAIL))
print(json.dumps({ 'slots':slots, 'front':save(sl, front, 'sleigh-front.png') }))

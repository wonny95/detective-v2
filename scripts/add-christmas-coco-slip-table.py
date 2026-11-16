"""Coco's hand-over slip as a folded note on her snowflake table (user request 2026-11-16: the slip drawn by the game
looked forced; folded on the table, unfolded in the close look 'cocoslip'). Higgsfield drew the note onto a crop of
the table (coco-table-higgsfield-original.png, from tent.jpg 960,384–1376,768 at about 2.4x); its re-drawn crop does
not line up with the picture, so only the note is cut out, made 82% as big and set 6 px right and 16 px higher into the empty corner
of the table top, clear of the snowflakes. The cut follows the note's dark outline a few pixels outside it, in the
drawing's own size (user report: the first cut, done small, lost the outline on the top and left).
Run from the project folder on the tent picture without the note: python scripts/add-christmas-coco-slip-table.py"""
from PIL import Image, ImageDraw, ImageFilter
X0, Y0, CW, CH = 960, 384, 416, 384            # the table crop in tent.jpg
tent = Image.open('assets/places/christmas/tent.jpg').convert('RGB')
ed = Image.open('assets/places/christmas/coco-table-higgsfield-original.png').convert('RGB')
sx, sy = CW / ed.width, CH / ed.height         # the drawing's pixels to the crop's
# the note's outline in the drawing's pixels: both halves, the fold's gap and the line round them
hull = [(757, 310), (857, 327), (858, 357), (776, 419), (672, 386)]
box = (664, 302, 866, 428)
mask = Image.new('L', ed.size, 0)
ImageDraw.Draw(mask).polygon(hull, 255)
note, nmask = ed.crop(box), mask.crop(box).filter(ImageFilter.GaussianBlur(1.5))
k, dx, dy = .82, 6, -16
w, h = round(note.width * sx * k), round(note.height * sy * k)
note, nmask = note.resize((w, h), Image.LANCZOS), nmask.resize((w, h), Image.LANCZOS)
cx, cy = (box[0] + box[2]) / 2 * sx, (box[1] + box[3]) / 2 * sy
at = (round(X0 + cx - w / 2 + dx), round(Y0 + cy - h / 2 + dy))
tent.paste(note, at, nmask)
tent.save('assets/places/christmas/tent.jpg', quality=92)
print('note at', at, (w, h))

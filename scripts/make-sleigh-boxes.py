"""Christmas case: the five gift boxes on the sleigh drawn one by one over an empty sleigh (user request 2026-11-16: an
opened box showed the closed one under it, and the star's box and the mittens' boxes must look exactly the same).
- sleigh-empty.jpg: sleigh.jpg with the boxes' part replaced by the Higgsfield edit of the crop (380, 320)-(1100, 800)
  with every box taken away (sleigh-empty-higgsfield-original.png), its edge faded.
- sleigh-rail.png: the front rail and its scroll cut out of sleigh-empty.jpg (a polygon along its top edge), drawn over
  the boxes so the back right ones stand behind it as in the old picture. Placed at RAIL_AT.
- One box, four looks, all from the same Higgsfield box (box-star-higgsfield-original.png and its edits) on flat grey,
  cut out as scripts/cut-christmas-stars.py does: box-closed.png (box-shut-…, lid on), box-mittens.png (mittens in it),
  box-star.png and box-empty.png as they are. The three open ones share box-star.png's size, so they lie on one place.
Run from the project folder."""
import importlib.util
from PIL import Image, ImageDraw, ImageFilter

D = 'assets/places/christmas/'
spec = importlib.util.spec_from_file_location('fix', 'scripts/fix-sleigh-open-box.py')
# only its cut_grey (the module also rebuilds its own pictures when run, which is harmless: same inputs, same result)
src = open('scripts/fix-sleigh-open-box.py', encoding='utf-8').read()
ns = {}; exec(src.split('# the sleigh without the middle box')[0], ns)
cut_grey = ns['cut_grey']

CROP = (380, 320, 1100, 800)
sl = Image.open(D + 'sleigh.jpg').convert('RGB')
w, h = CROP[2] - CROP[0], CROP[3] - CROP[1]
ed = Image.open(D + 'sleigh-empty-higgsfield-original.png').convert('RGB').resize((w, h), Image.LANCZOS)
mask = Image.new('L', (w, h)); ImageDraw.Draw(mask).rectangle((36, 56, 676, 372), fill=255)   # the boxes, (416, 376)-(1056, 692)
mask = mask.filter(ImageFilter.GaussianBlur(10))
part = sl.crop(CROP); part.paste(ed, (0, 0), mask); sl.paste(part, CROP[:2])
sl.save(D + 'sleigh-empty.jpg', quality=92)

# the front rail over the boxes: its top edge from the scroll to the right, down its inner edge to the floor
RAIL = [(836, 652), (842, 622), (852, 604), (872, 594), (900, 590), (960, 574), (1020, 556), (1080, 536), (1110, 526),
        (1110, 720), (800, 720), (812, 690), (826, 668)]
m = Image.new('L', sl.size); ImageDraw.Draw(m).polygon(RAIL, fill=255)
rail = sl.convert('RGBA'); rail.putalpha(m)
box = m.getbbox(); rail.crop(box).save(D + 'sleigh-rail.png')
print('rail at', box)

size = Image.open(D + 'box-star.png').size
cut_grey('box-mittens-open-higgsfield-original.png', size).save(D + 'box-mittens.png')
closed = cut_grey('box-shut-higgsfield-original.png', (1024, 688))
closed = closed.crop(closed.getchannel('A').point(lambda v: 255 if v > 24 else 0).getbbox())
closed.save(D + 'box-closed.png'); print('closed', closed.size)

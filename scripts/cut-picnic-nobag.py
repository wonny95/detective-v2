"""The picnic table without Rosie's backpack, for while the bag is with the detective (user request: the bag on the table
goes once Rosie hands it over). One Higgsfield edit of the table's crop (picnic-wide.png 890..1190 x 235..460 scaled to
1024x768, Nano Banana 2.1, job 4ad63d5e-765a-43a4-bacd-a0348d7e7531) -> picnic-nobag-higgsfield-original.png. It lines
up with a plain resize; only where it differs from the picture (the backpack and its shadow) is kept, grown and softened
so it fades into the drawing -> assets/places/picnic-storyboard/picnic-nobag.png, drawn over picnic-wide.png at the
printed x, y."""
from PIL import Image, ImageChops, ImageDraw, ImageFilter
D = 'assets/places/picnic-storyboard/'
BOX = (890, 235, 1190, 460)
src = Image.open(D + 'picnic-wide.png').convert('RGB').crop(BOX)
ed = Image.open(D + 'picnic-nobag-higgsfield-original.png').convert('RGB').resize(src.size, Image.LANCZOS)
hit = ImageChops.difference(src, ed).convert('L').point(lambda v: 255 if v > 30 else 0)
# only around the backpack (its loop to its strap and the table under it), not the small redraws elsewhere
keep = Image.new('L', src.size); ImageDraw.Draw(keep).rectangle((60, 45, 235, 215), fill=255)
hit = ImageChops.multiply(hit, keep)
mask = hit.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(3))
patch = ed.convert('RGBA'); patch.putalpha(mask)
tb = mask.point(lambda v: 255 if v > 2 else 0).getbbox()
patch.crop(tb).save(D + 'picnic-nobag.png', optimize=True)
print('picnic-nobag.png', 'x', BOX[0] + tb[0], 'y', BOX[1] + tb[1], 'w', tb[2] - tb[0], 'h', tb[3] - tb[1])

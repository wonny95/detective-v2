"""Review 2 and 3 of the Christmas case: the sack by the sleigh is tied shut (no wrapped gifts to count) and Tess's
table seen inside the tent is the one in the tent picture (kraft-paper gifts, an open box, the clipboard). Higgsfield
edited the whole scene (assets/places/christmas/sleigh-fix-higgsfield-original.png); only those two areas are pasted
back over sleigh.jpg with soft edges, so every spot and photo crop stays where it was.
Run from the project folder with the old sleigh.jpg as the argument: python scripts/fix-christmas-sleigh.py <old.jpg>"""
import sys
from PIL import Image, ImageDraw, ImageFilter
old = Image.open(sys.argv[1]).convert('RGB')
fix = Image.open('assets/places/christmas/sleigh-fix-higgsfield-original.png').convert('RGB').resize(old.size, Image.LANCZOS)
mask = Image.new('L', old.size, 0)
d = ImageDraw.Draw(mask)
d.rectangle((945, 250, 1268, 560), 255)   # inside the tent: the table
d.rectangle((448, 715, 715, 1012), 255)   # the sack
mask = mask.filter(ImageFilter.GaussianBlur(8))
old.paste(fix, (0, 0), mask)
old.save('assets/places/christmas/sleigh.jpg', quality=92)

# The decorated day square (user request): Higgsfield edit of tree-higgsfield-original.jpg with more ornaments,
# tree-decorated-higgsfield-original.png (896x1200, its tree sits lower than the old one). Scaled to 1376x1843 as
# scripts/cut-christmas-assets.py does; the band starts at 400 (not 330) so the tree's foot stays at the same height
# in the picture; the rest is the floor (675 high, the old one 745). The case list photo is its upper 4:3.
# Run from the project folder: python scripts/make-christmas-decorated-tree.py [old-day.jpg old-night.jpg]
from PIL import Image
D = 'assets/places/christmas/'
src = Image.open(D + 'tree-decorated-higgsfield-original.png').convert('RGB')
im = src.resize((1376, 1843), Image.LANCZOS)
TOP = 400
im.crop((0, TOP, 1376, TOP + 768)).save(D + 'tree.jpg', quality=88)
im.crop((0, TOP + 768, 1376, 1843)).save(D + 'tree-floor.jpg', quality=85)
src.crop((0, 80, 896, 752)).resize((800, 600), Image.LANCZOS).save(D + 'tree-cover.jpg', quality=86)
print('floor', 1843 - TOP - 768)

# The lit square to match (user request): Higgsfield edit of the decorated picture with 144 px of plain sky added on
# top (so the gold star fits), tree-lit-decorated-higgsfield-original.png (848x1264, as tall as that padded picture).
# Scaled to 1376x2064 so it lines up with the day one: the day band starts 400 + 221 down, above it the lit sky.
lit = Image.open(D + 'tree-lit-decorated-higgsfield-original.png').convert('RGB').resize((1376, 2064), Image.LANCZOS)
LTOP = TOP + 221
lit.crop((0, 0, 1376, LTOP)).save(D + 'tree-lit-sky.jpg', quality=88)
lit.crop((0, LTOP, 1376, LTOP + 768)).save(D + 'tree-lit.jpg', quality=88)
lit.crop((0, LTOP + 768, 1376, 2064)).save(D + 'tree-floor-lit.jpg', quality=85)
print('lit sky', LTOP, 'floor', 2064 - LTOP - 768)

# The night square (before the lighting): the day one darkened the way the first night picture was made from the
# first day picture: each colour channel mapped from that day picture's mean and spread to the night one's
# (old-day.jpg / old-night.jpg: the first day and night pictures, from git ea4f09c, passed as arguments)
import sys
from PIL import ImageStat
if len(sys.argv) > 2:
    s, t = ImageStat.Stat(Image.open(sys.argv[1]).convert('RGB')), ImageStat.Stat(Image.open(sys.argv[2]).convert('RGB'))
    def night(im):
        return Image.merge('RGB', [b.point(lambda v, c=c: max(0, min(255, round((v - s.mean[c]) * t.stddev[c] / s.stddev[c] + t.mean[c]))))
                                   for c, b in enumerate(im.split())])
    night(Image.open(D + 'tree.jpg').convert('RGB')).save(D + 'tree-night.jpg', quality=88)
    night(Image.open(D + 'tree-floor.jpg').convert('RGB')).save(D + 'tree-floor-night.jpg', quality=88)
    print('night made')

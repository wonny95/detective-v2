# The decorated day square (user request): Higgsfield edit of tree-higgsfield-original.jpg with more ornaments,
# tree-decorated-higgsfield-original.png (896x1200, its tree sits lower than the old one). Scaled to 1376x1843 as
# scripts/cut-christmas-assets.py does; the band starts at 400 (not 330) so the tree's foot stays at the same height
# in the picture; the rest is the floor (675 high, the old one 745). The case list photo is its upper 4:3.
# Run from the project folder: python scripts/make-christmas-decorated-tree.py
from PIL import Image
D = 'assets/places/christmas/'
src = Image.open(D + 'tree-decorated-higgsfield-original.png').convert('RGB')
im = src.resize((1376, 1843), Image.LANCZOS)
TOP = 400
im.crop((0, TOP, 1376, TOP + 768)).save(D + 'tree.jpg', quality=88)
im.crop((0, TOP + 768, 1376, 1843)).save(D + 'tree-floor.jpg', quality=85)
src.crop((0, 80, 896, 752)).resize((800, 600), Image.LANCZOS).save(D + 'tree-cover.jpg', quality=86)
print('floor', 1843 - TOP - 768)

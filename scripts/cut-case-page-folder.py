"""Cut the case page's folder and paper (mockup 4) out of the Higgsfield sheet on magenta.

Sheets: v1 job 37bd5ce8-5e82-4a59-a7fd-798df22ad1b0, v2 job 205d57a8-a8e6-4d18-881e-fc556522e01f, v3 job 4d8f3e91-64b1-40b6-8b01-8c07d6e421f6 (nano_banana_2_1 16:9 1K)
-> assets/ui/case-page-folder.webp (kraft folder back with its index tab), assets/ui/case-page-paper.webp (cream sheet)
Magenta is taken out by how magenta a pixel is (alpha), and its tint is pulled out of the edge colours. PIL only.
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SHEETS = {
    'v1': ROOT / 'assets/ui/case-page-folder-higgsfield-original.png',      # job 37bd5ce8: folder (tab looked two-tier) + paper
    'v2': ROOT / 'assets/ui/case-page-folder-v2-higgsfield-original.png',   # job 205d57a8: smooth paper (its folder unusable)
    'v3': ROOT / 'assets/ui/case-page-folder-v3-higgsfield-original.png',   # job 4d8f3e91: open folder back, tall tab on top (from a shape guide)
}


def unmagenta(px):
    r, g, b = px
    mag = min(1.0, max(0.0, ((r + b) / 2 - g - 40) / 140))   # high red and blue, low green
    al = 1 - mag
    if al <= 0.02:
        return (0, 0, 0, 0)
    un = lambda v, m: int(min(255, max(0, (v - m * (1 - al)) / al)))
    return (un(r, 255), un(g, 0), un(b, 255), int(al * 255))


def cut(sheet, box, name):
    piece = Image.open(SHEETS[sheet]).convert('RGB').crop(box)
    out = Image.new('RGBA', piece.size)
    out.putdata([unmagenta(p) for p in piece.getdata()])
    bbox = out.getchannel('A').point(lambda v: 255 if v > 24 else 0).getbbox()
    out = out.crop(bbox)
    out.save(ROOT / 'assets/ui' / name, 'WEBP', quality=90)
    print(name, out.size)


cut('v3', (330, 20, 1050, 768), 'case-page-folder.webp')   # user: v1's tab looked two-tier (a closed folder's flap)
cut('v2', (720, 0, 1330, 768), 'case-page-paper.webp')   # user: v1 paper's edges were too jagged

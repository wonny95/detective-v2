"""The spelling game's treasure chest (user request 2026-11-23: the padlock hangs on the chest; the lock keeps its size
and place, the chest is scaled behind it and may run out of the frame; no acorns in the open chest, light only).
Nano Banana 2.1 3:4: wide chest job 0fc816a6-ac01-4e53-930b-248b470147bc (with a knocker ring the user found odd),
edited to a hinged hasp plate with a small iron staple, job a013f07f-900d-45cc-95cc-501cc137303e
-> assets/ui/chest3-closed-higgsfield-original.png; open (light only) job 4e7e3802-3647-4e81-8db0-c36fb64db583
-> assets/ui/chest2-open-higgsfield-original.png (896x1200 both).
Writes assets/ui/chest-closed.webp, chest-open.webp (the whole picture) and chest-staple.webp: the staple alone (a solid
pill seen end-on: its whole body is kept), laid over the padlock so the shackle looks threaded through it.
Staple (picture px): x 436-460, y 676-747. index.html places the chest so the shackle top sits
at y 692 inside the hole (.sg-chest).
Run from the project folder: python -I scripts/cut-chest.py"""
from PIL import Image, ImageFilter
Image.open('assets/ui/chest3-closed-higgsfield-original.png').convert('RGB').save('assets/ui/chest-closed.webp', quality=88)
Image.open('assets/ui/chest2-open-higgsfield-original.png').convert('RGB').save('assets/ui/chest-open.webp', quality=88)
im = Image.open('assets/ui/chest3-closed-higgsfield-original.png').convert('RGB')
mask = Image.new('L', im.size); mp = mask.load()
R, X, Y0, Y1 = 14, 448, 676 + 13, 747 - 13      # a stadium: within R of the pill's centre line
for y in range(665, 760):
    for x in range(425, 472):
        if abs(x - X) <= R and Y0 - R <= y <= Y1 + R and (Y0 <= y <= Y1 or min(abs(y - Y0), abs(y - Y1)) ** 2 + (x - X) ** 2 <= R * R):
            mp[x, y] = 255
mask = mask.filter(ImageFilter.GaussianBlur(.8))
st = im.convert('RGBA'); st.putalpha(mask)
st.save('assets/ui/chest-staple.webp', quality=90)
print('ok', mask.getbbox())

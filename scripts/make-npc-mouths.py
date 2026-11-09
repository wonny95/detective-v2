"""NPC talking mouths (assets/characters/mouths).

1. split_sheet(): mouths/sheet-original.png (one Higgsfield sheet, eight mouths on flat green) -> the eight mouths,
   green keyed out: smile, nervous, sad, beak, each with -open.
2. For each sprite, the drawn mouth is found (dark marks connected to its box; Fiona's nervous grin also its white
   teeth), painted over with the fur around it, and the new closed / open mouth is laid on that cover:
   <sprite>-closed.png, <sprite>-open.png. The closed line is thickened to the drawing's own weight.
   The duck's beak is replaced whole by the generated beaks.
3. The printed meta ([x, y, w, h] in sprite px) goes into MOUTHS in index.html.

   Ben's two front teeth hang under his smile, so his drawn mouth stays: closed = the picture as drawn, open =
   cut from a Higgsfield edit of his face with the mouth open (mouths/ben-open-higgsfield-original.png: the sprite's
   face 196..436 x 110..350 scaled to 1024, edited; the chin drops a little with it), its colours matched to the
   sprite and only where it differs from the drawing, edges blended (ben_mouth()).
   Mia and Ollie share one picture (mia): Ollie's mouth is mia-ollie.

Run: python -I scripts/make-npc-mouths.py [keys]   (Pillow only; no keys = all)
"""
import os, json
from collections import deque
from PIL import Image, ImageFilter, ImageChops, ImageDraw
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','assets','characters')+'/'
M=D+'mouths/'
# sprite: file, recorded mouth box (x centre, y top, w, h), mouth set, the drawing's line weight (px, by eye),
# top of the area searched for the drawn mouth (just under the nose; ray's and rosie's line from the nose stays)
S={'badger':('sgt-badger-higgsfield.png',538,643,156,64,'smile',7,612),
   'mole':('mole-higgsfield.png',207,211,56,23,'smile',3.5,197),
   'fiona':('fiona-higgsfield.png',179,225,48,24,'smile',3,216),
   'ray':('ray-higgsfield.png',192,205,49,24,'smile',4,194),
   'rosie':('rosie-higgsfield.png',161,339,24,17,'smile',2.6,333),
   'betty':('betty-higgsfield.png',224,210,66,16,'smile',2.6,205),
   'fiona-nervous':('fiona-nervous.png',200,230,52,22,'nervous',3,222),
   'fiona-sad':('fiona-sad.png',236,215,36,16,'sad',3,212),
   'detective':('detective-higgsfield.png',279,279,60,20,'smile',3.3,269),
   'detective-thinking':('detective-thinking.png',268,282,60,18,'smile',3.3,268),
   'detective-point':('detective-point.png',267,280,62,18,'smile',3.3,268),
   'detective-lens':('detective-lens.png',186,299,40,14,'smile',2.6,290),
   'detective-wave':('detective-wave.png',272,278,62,18,'smile',3.3,268),
   'nora':('nora-higgsfield.png',225,284,62,13,'smile',3,281),
   'mia':('mia-higgsfield.png',638,328,72,22,'smile',3.5,318),
   'mia-ollie':('mia-higgsfield.png',322,205,143,45,'smile',4.5,204),
   'tess':('tess-higgsfield.png',266,212,100,20,'smile',4,203),
   'ruby':('ruby-higgsfield.png',202,230,78,20,'smile',3,226),
   'ella':('ella-higgsfield.png',238,248,58,14,'smile',3,244),
   'finn':('finn-higgsfield.png',209,155,175,35,'smile',4.5,145),
   # the violin case (2026-11-08); search tops just under the nose, so the line from it stays
   'tara':('tara-higgsfield.png',277,220,80,14,'smile',3.5,212),
   'owen':('owen-higgsfield.png',219,214,82,18,'smile',3,213),
   'ivo':('ivo-higgsfield.png',228,260,63,13,'smile',3,259),
   'momo':('momo-higgsfield.png',210,213,85,22,'smile',4,211),
   'owen-nervous':('owen-nervous-higgsfield.png',221,223,90,14,'nervous',3,212),
   'owen-sad':('owen-sad-higgsfield.png',221,225,52,16,'sad',3,216)}
import sys
if sys.argv[1:]: S={k:v for k,v in S.items() if k in sys.argv[1:]}
NEAR=('mia-ollie','finn')   # mouths whose curled ends break off; the others are one line, and the box would also take in fur texture
# only cover within the recorded box (a few px around): on these pictures the crayon texture links the mouth to the
# cheeks and whiskers
LIMIT=('nora','mia','mia-ollie','tess','ruby','ella','finn','tara','owen','ivo','momo','owen-nervous','owen-sad')
DARK={'mia':50}   # how much darker than the fur around a mark must be (default 22); Mia's white muzzle has crayon grain
KEEP={'badger':(466,600,604,627),'detective':(256,250,298,274),'detective-thinking':(248,252,288,276),
      'detective-point':(245,250,284,274),'detective-lens':(160,270,196,295),'detective-wave':(251,250,291,276),
      'mia-ollie':(290,150,356,205),'mia':(629,318,637,341),'ruby':(185,200,220,226),'ella':(212,212,262,244)}
# areas never covered (sprite px): the badger's nose sits right above the curled mouth ends; Ollie's nose, Mia's line from the nose
# the umbrella case: the closed mouth stays as drawn (the cat's and the deer's mouth under the nose, Tess's and Finn's
# smile), only the open one is new
# the violin case's too (the ferret's wavy line, the fox's and the goat's mouth under the nose, Owen's wobbly and sad
# mouths)
AS_DRAWN=('tess','ruby','ella','finn','tara','owen','ivo','momo','owen-nervous','owen-sad')
SRC_LINE=6   # line weight of the closed mouths in the sheet (px)
L=lambda im: im.convert('L')

def components(hit, seed):
    """pixels of hit (L, 255 = on) connected to any on-pixel inside seed box"""
    W,H=hit.size; p=hit.load(); out=Image.new('L',hit.size,0); o=out.load()
    q=deque((i,j) for i in range(max(0,seed[0]),min(W,seed[2])) for j in range(max(0,seed[1]),min(H,seed[3])) if p[i,j])
    for i,j in q: o[i,j]=255
    while q:
        i,j=q.popleft()
        for di in (-1,0,1):
            for dj in (-1,0,1):
                a,b=i+di,j+dj
                if 0<=a<W and 0<=b<H and p[a,b] and not o[a,b]: o[a,b]=255; q.append((a,b))
    return out

def fill_from_around(reg, hole, r):
    """colour inside hole from the blurred colour of the fur around it (normalised blur); darker marks (the nose,
    other lines) are left out so they do not stain it"""
    lr=reg.convert('L'); base=sorted(lr.get_flattened_data())[lr.size[0]*lr.size[1]//2]
    keep=ImageChops.multiply(ImageChops.invert(hole),lr.point(lambda v:255 if v>base-35 else 0))
    rgb=reg.convert('RGB'); chans=[]
    kb=keep.filter(ImageFilter.GaussianBlur(r))
    kd=list(kb.get_flattened_data())
    for c in rgb.split():
        nb=ImageChops.multiply(c,keep).filter(ImageFilter.GaussianBlur(r))   # premultiplied by keep
        out=Image.new('L',c.size); out.putdata([min(255,n*255//max(k,1)) for n,k in zip(nb.get_flattened_data(),kd)])
        chans.append(out)
    return Image.merge('RGB',chans).convert('RGBA')

CUT={}  # the sheet's mouths, cut by split_sheet()

def closed_art(name, tw, line, ink):
    m=CUT[name]
    need=line*m.size[0]/tw; steps=int(round((need-SRC_LINE)/2))
    a=m.getchannel('A')
    for _ in range(max(0,steps)): a=a.filter(ImageFilter.MaxFilter(3))
    if steps>0: a=a.filter(ImageFilter.GaussianBlur(1.2)).point(lambda v: 0 if v<60 else min(255,int((v-60)*255/120)))
    out=Image.new('RGBA',m.size,ink+(0,)); out.putalpha(a)
    th=max(1,int(m.size[1]*tw/m.size[0])); return out.resize((tw,th),Image.LANCZOS)

def open_art(name, tw):
    m=CUT[name]; th=max(1,int(m.size[1]*tw/m.size[0])); return m.resize((tw,th),Image.LANCZOS)

def split_sheet():
    src=Image.open(M+'sheet-original.png').convert('RGB')
    W,H=src.size
    px=src.load()
    out=Image.new('RGBA',src.size)
    op=out.load()
    for y in range(H):
        for x in range(W):
            r,g,b=px[x,y]
            m=max(r,b)
            spill=g-m
            a=255 if spill<=20 else max(0,255-int((spill-20)*255/90))
            if g>m: g=m+max(0,min(spill,8))  # despill
            op[x,y]=(r,min(g,255),b,a)
    names=['smile','smile-open','nervous','nervous-open','sad','sad-open','beak','beak-open']
    cw,ch=W//4,H//2
    for i,n in enumerate(names):
        cx,cy=(i%4)*cw,(i//4)*ch
        cell=out.crop((cx,cy,cx+cw,cy+ch))
        bb=cell.getchannel('A').point(lambda v:255 if v>40 else 0).getbbox()
        pad=6
        bb=(max(bb[0]-pad,0),max(bb[1]-pad,0),min(bb[2]+pad,cw),min(bb[3]+pad,ch))
        c=cell.crop(bb)
        CUT[n]=c.convert('RGBA')
        print(n,c.size)

split_sheet()
meta={}
for key,(f,x,y,w,h,kind,line,top) in S.items():
    im=Image.open(D+f).convert('RGBA')
    x0,y0,x1,y1=int(x-w*1.5),top,int(x+w*1.5),int(y+h*2.2)   # top: just under the nose (the mouth's curled ends reach above its box)
    reg=im.crop((x0,y0,x1,y1))
    k=max(9,int(h*.6))|1
    med=reg
    for _ in range(3): med=med.filter(ImageFilter.MedianFilter(k))
    lr,lm=L(reg),L(med)
    dark=ImageChops.subtract(lm,lr).point(lambda v,t=DARK.get(key,22):255 if v>t else 0)
    bright=ImageChops.subtract(lr,lm).point(lambda v:255 if v>22 else 0) if kind=='nervous' else Image.new('L',reg.size,0)
    hit=ImageChops.lighter(dark,bright)
    if key in KEEP:   # the nose stays as drawn
        kx0,ky0,kx1,ky1=KEEP[key]; ImageDraw.Draw(hit).rectangle((kx0-x0,ky0-y0,kx1-x0,ky1-y0),fill=0)
    seed=(int(x-w*.3)-x0,int(y)-y0,int(x+w*.3)-x0,int(y+h)-y0)
    comp=components(hit,seed)
    bb=comp.getbbox()
    # bits of the same mouth that break off (the curled ends): every mark inside its box, a few px around
    if key in LIMIT:
        lim=Image.new('L',reg.size,0); ImageDraw.Draw(lim).rectangle((x-w/2-8-x0,0,x+w/2+8-x0,y+h+8-y0),fill=255)
        comp=ImageChops.multiply(comp,lim); hit=ImageChops.multiply(hit,lim); bb=comp.getbbox()
    if key in NEAR:
        near=Image.new('L',reg.size,0); ImageDraw.Draw(near).rectangle((bb[0]-14,bb[1]-7,bb[2]+14,bb[3]+5),fill=255)
        comp=ImageChops.lighter(comp,ImageChops.multiply(hit,near)); bb=comp.getbbox()
    hole=comp.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.MinFilter(5))
    if kind=='nervous':   # the white teeth inside the grin: cover the whole grin
        e=Image.new('L',reg.size,0); ImageDraw.Draw(e).ellipse((bb[0]-2,bb[1]-2,bb[2]+2,bb[3]+2),fill=255); hole=ImageChops.lighter(hole,e)
    fill=fill_from_around(reg,hole,max(6,(bb[3]-bb[1])*.7))
    mask=hole.filter(ImageFilter.GaussianBlur(1.5))
    cover=fill.copy(); cover.putalpha(ImageChops.multiply(mask,reg.getchannel('A')))
    # the new mouth sits where the drawn one was: same width, same middle
    cw=bb[2]-bb[0]; cx=x0+(bb[0]+bb[2])/2; cy=y0+(bb[1]+bb[3])/2
    ink=(58,40,34)
    for state in ['closed','open']:
        if state=='closed': art=closed_art(kind,int(cw*1.0),line,ink); ay=cy-art.size[1]/2
        else: art=open_art(kind+'-open',int(cw*(.95 if kind=='nervous' else .8))); ay=cy-art.size[1]*(.45 if kind=='nervous' else .3)
        layer=cover.copy()
        layer.alpha_composite(art,(int(cx-art.size[0]/2)-x0,int(ay)-y0))
        # trim to what is drawn
        tb=layer.getchannel('A').getbbox()
        layer.crop(tb).save(M+f'{key}-{state}.png',optimize=True)
        meta.setdefault(key,{})[state]=[x0+tb[0],y0+tb[1],tb[2]-tb[0],tb[3]-tb[1]]
    if key in AS_DRAWN:   # the closed mouth is the picture as drawn, over the same box
        r=meta[key]['closed']; im.crop((r[0],r[1],r[0]+r[2],r[1]+r[3])).save(M+f'{key}-closed.png',optimize=True)
    print(key,'drawn mouth',[x0+bb[0],y0+bb[1],cw,bb[3]-bb[1]],meta[key])
def ben_mouth():
    im=Image.open(D+'ben-higgsfield.png').convert('RGBA'); box=(236,222,396,292)   # smile 260..373 x 240..255, teeth 293..340 x 247..279
    reg=im.crop(box); reg.save(M+'ben-closed.png',optimize=True)
    face=(196,110,436,350)   # the square the edit was made from
    src=im.crop(face).convert('RGB'); ed=Image.open(M+'ben-open-higgsfield-original.png').convert('RGB').resize(src.size,Image.LANCZOS)
    # colours: the edit is a little more orange; match it to the drawing on the untouched upper face
    up=(20,10,220,120); ms=[sum(c)/len(c) for c in zip(*src.crop(up).getdata())]; me=[sum(c)/len(c) for c in zip(*ed.crop(up).getdata())]
    ed=Image.merge('RGB',[ch.point(lambda v,g=ms[i]/me[i]:min(255,round(v*g))) for i,ch in enumerate(ed.split())])
    # only where the edit differs (mouth and the lower chin), grown and softened so it fades into the drawing
    hit=ImageChops.difference(src,ed).convert('L').point(lambda v:255 if v>28 else 0)
    keep=Image.new('L',src.size,0); ImageDraw.Draw(keep).rectangle((70,135,175,215),fill=255); hit=ImageChops.multiply(hit,keep)
    mask=hit.filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.GaussianBlur(2.5))
    layer=ed.convert('RGBA'); layer.putalpha(ImageChops.multiply(mask,im.crop(face).getchannel('A')))
    tb=layer.getchannel('A').point(lambda v:255 if v>2 else 0).getbbox()
    layer.crop(tb).save(M+'ben-open.png',optimize=True)
    meta['ben']={'closed':[box[0],box[1],box[2]-box[0],box[3]-box[1]],'open':[face[0]+tb[0],face[1]+tb[1],tb[2]-tb[0],tb[3]-tb[1]]}; print('ben',meta['ben'])
if not sys.argv[1:] or 'ben' in sys.argv[1:]: ben_mouth()
def pip_mouth():
    """Pip the sparrow talks with his beak: closed = as drawn; open = the lower half (under the line across it, y 216)
    dropped 6 px, the gap the dark inside of the beak, only across the beak's own width at that line"""
    im=Image.open(D+'pip-higgsfield.png').convert('RGBA'); box=(186,176,284,250); split=216; drop=6
    reg=im.crop(box); reg.save(M+'pip-closed.png',optimize=True)
    W,H=reg.size; s=split-box[1]; out=reg.copy()
    out.paste(reg.crop((0,s,W,H-drop)),(0,s+drop))
    row=[reg.getpixel((i,s)) for i in range(W)]; dark=[i for i,p in enumerate(row) if sum(p[:3])<330]
    d=ImageDraw.Draw(out); d.rectangle((min(dark),s,max(dark),s+drop),fill=(70,38,36,255))
    out.save(M+'pip-open.png',optimize=True)
    meta['pip']={'closed':[box[0],box[1],W,H],'open':[box[0],box[1],W,H]}; print('pip',meta['pip'])
if not sys.argv[1:] or 'pip' in sys.argv[1:]: pip_mouth()
# duck: the generated beaks replace the drawn one (147..300 x 167..248)
for state,name in [('closed','beak'),('open','beak-open')] if not sys.argv[1:] or 'duck' in sys.argv[1:] else []:
    m=CUT[name]; BW=166; th=int(m.size[1]*BW/m.size[0]*0.9)
    m=m.resize((BW,th),Image.LANCZOS); m.save(M+f'duck-{state}.png',optimize=True)
    meta.setdefault('duck',{})[state]=[223-83,160,BW,th]
print(json.dumps(meta))
# meta: the [x, y, w, h] that go into MOUTHS in index.html
def prev(key,f,state):
    im=Image.open(D+f).convert('RGBA'); mt=meta[key]['closed']
    if state!='orig':
        r=meta[key][state]; im.alpha_composite(Image.open(M+f'{key}-{state}.png'),(r[0],r[1]))
    cx=mt[0]+mt[2]//2; cy=mt[1]+mt[3]//2; pad=int(max(mt[2],40)*.9)
    c=im.crop((cx-pad,cy-pad,cx+pad,cy+pad)).resize((200,200),Image.LANCZOS); bg=Image.new('RGBA',c.size,(150,150,150,255)); bg.alpha_composite(c); return bg
tiles=[]
if 'ben' in meta:
    for st in ['orig','closed','open']: tiles.append(prev('ben','ben-higgsfield.png',st))
for key,v in S.items():
    for st in ['orig','closed','open']: tiles.append(prev(key,v[0],st))
if 'duck' in meta:
    for st in ['orig','closed','open']: tiles.append(prev('duck','duck-higgsfield.png',st))
sheet=Image.new('RGB',(600,200*len(tiles)//3),'white')
for i,t in enumerate(tiles): sheet.paste(t.convert('RGB'),((i%3)*200,(i//3)*200))
sheet.save(os.path.join(os.environ.get("TEMP","."),"mouth-preview.png"))   # orig | closed | open, row per sprite

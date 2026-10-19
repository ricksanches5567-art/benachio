# Imagem de compartilhamento (og.jpg, 1200x630) da Benachio: painel café à esquerda + bolsa à direita.
import numpy as np
from PIL import Image, ImageDraw, ImageFont
FONT='/usr/share/fonts/truetype/sand-box/google/Cormorant Garamond/CormorantGaramond-VariableFont_wght.ttf'
def font(sz,w=600):
    f=ImageFont.truetype(FONT,sz)
    try: f.set_variation_by_axes([w])
    except Exception: pass
    return f
def tracked(d,xy,t,f,fill,sp):
    x,y=xy
    for c in t: d.text((x,y),c,font=f,fill=fill); x+=d.textlength(c,font=f)+sp
W,H=1200,630
src=Image.open('/workspace/bolsas-src/gen/20.jpg').convert('RGB'); sw,sh=src.size
shift=300; a=np.pad(np.asarray(src),((0,0),(shift,0),(0,0)),mode='edge')[:, :sw]
im=Image.fromarray(a).resize((int(sw*H/sh),H),Image.LANCZOS)
canvas=Image.new('RGB',(W,H),(36,21,15)); canvas.paste(im,(W-im.width,0))
arr=np.asarray(canvas).astype(np.float32); x=np.arange(W)[None,:,None]
k=np.clip(1-(x-420)/320,0,1)**1.2; k=np.where(x<420,1,k)
arr=arr*(1-k)+np.array([36,21,15],dtype=np.float32)*k
canvas=Image.fromarray(arr.astype(np.uint8)); d=ImageDraw.Draw(canvas)
tracked(d,(64,215),'BENACHIO',font(92,500),(247,238,224),8)
d.line((68,350,168,350),fill=(214,170,106),width=2)
tracked(d,(66,372),'BOLSAS · CURITIBA',font(34,600),(214,170,106),8)
canvas.save('img/og.jpg',quality=90)

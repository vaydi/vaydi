import sys, os, textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H=1280,720
B="/usr/share/fonts/opentype/inter/Inter-Black.otf"
R="/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
out=sys.argv[1]
def bg():
    im=Image.new("RGB",(W,H))
    d=ImageDraw.Draw(im)
    for y in range(H):
        t=y/H
        d.line([(0,y),(W,y)],fill=(int(40+150*t),int(10+20*t),int(90+40*(1-t))))
    glow=Image.new("RGB",(W,H));g=ImageDraw.Draw(glow)
    g.ellipse([W-520,-200,W+200,420],fill=(255,80,180));g.ellipse([-250,H-300,350,H+250],fill=(60,200,255))
    return Image.blend(im,glow.filter(ImageFilter.GaussianBlur(160)),0.45)
def badge(d):
    f=ImageFont.truetype(B,26);d.rounded_rectangle([40,36,300,84],12,fill=(0,0,0,));d.text((58,44),"VAYDI GAMING",font=f,fill=(255,120,200))
slides=[
 ("J-18","GTA VI : TOUT ce qu'il faut savoir avant le 19 novembre"),
 ("ACCROCHE","Dans moins de trois semaines, le jeu le plus attendu de la décennie sort enfin."),
 ("DATE","19 novembre 2026 — PS5 et Xbox Series X|S. Pas de PC au lancement."),
 ("12+ ANS","GTA V est sorti en 2013. Le jeu a été repoussé plusieurs fois avant cette date."),
 ("LA CARTE","Retour à Vice City, dans Leonida, un État inspiré de la Floride."),
 ("LE DUO","Lucia et Jason, un couple façon Bonnie et Clyde."),
 ("À VENIR","Prix, taille du jeu, GTA Online… on en reparle dès que Rockstar parle."),
 ("ET TOI ?","Lucia ou Jason ? Dis-le en commentaire. Abonne-toi et active la cloche !"),
]
os.makedirs(out,exist_ok=True)
for i,(big,txt) in enumerate(slides):
    im=bg();d=ImageDraw.Draw(im);badge(d)
    fb=ImageFont.truetype(B,150 if len(big)<8 else 110)
    d.text((W/2+5,H/2-95),big,font=fb,fill=(0,0,0),anchor="mm")
    d.text((W/2,H/2-100),big,font=fb,fill=(255,255,255),anchor="mm")
    fr=ImageFont.truetype(R,40)
    lines=textwrap.wrap(txt,42)
    for k,l in enumerate(lines):
        d.text((W/2,H/2+50+k*54),l,font=fr,fill=(255,235,250),anchor="mm")
    d.text((W-40,H-30),f"{i+1}/{len(slides)}  •  aperçu",font=ImageFont.truetype(R,20),fill=(255,255,255),anchor="rs")
    im.save(f"{out}/s{i:02d}.png")
# miniature
im=bg();d=ImageDraw.Draw(im)
f=ImageFont.truetype(B,190)
for dx,dy,c in [(8,8,(0,0,0)),(0,0,(255,255,255))]:
    d.text((60+dx,170+dy),"GTA VI",font=f,fill=c)
f2=ImageFont.truetype(B,120);d.rounded_rectangle([60,430,560,590],24,fill=(255,40,140));d.text((310,510),"J-18",font=f2,fill="white",anchor="mm")
d.text((620,470),"TOUT CE\nQU'ON SAIT",font=ImageFont.truetype(B,64),fill=(255,230,120),spacing=6)
d.text((60,60),"VAYDI GAMING",font=ImageFont.truetype(B,40),fill=(255,120,200))
im.save(f"{out}/miniature.png")

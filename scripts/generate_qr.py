from pathlib import Path
import argparse
from urllib.parse import urlparse
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.pdfgen import canvas
from PIL import Image, ImageDraw
p=argparse.ArgumentParser(description='Generate PNG and vector PDF QR for a website URL')
p.add_argument('url',help='Public website URL, or LAN URL for local testing')
a=p.parse_args()
if urlparse(a.url).scheme not in ('http','https'): p.error('Use an http:// or https:// URL')
out=Path(__file__).resolve().parents[1]/'qr';out.mkdir(exist_ok=True)
q=QrCodeWidget(a.url);q.qr.make();m=q.qr.modules;n=len(m);b=4;s=8;size=(n+8)*s
c=canvas.Canvas(str(out/'generated-qr.pdf'),pagesize=(size,size+70));c.setTitle('Haier Model List QR')
c.setFont('Helvetica-Bold',16);c.drawCentredString(size/2,size+43,'Haier Heater Labels')
c.setFont('Helvetica',10);c.drawCentredString(size/2,size+25,'Scan, select your model, view the sticker')
im=Image.new('RGB',((n+8)*20,)*2,'white');d=ImageDraw.Draw(im)
for y,row in enumerate(m):
    for x,v in enumerate(row):
        if v:
            c.rect((x+b)*s,(n-1-y+b)*s,s,s,fill=1,stroke=0)
            d.rectangle(((x+b)*20,(y+b)*20,(x+b+1)*20-1,(y+b+1)*20-1),fill='black')
c.linkURL(a.url,(0,0,size,size),relative=0,thickness=0);c.save();im.save(out/'generated-qr.png')
print('Saved qr/generated-qr.pdf and qr/generated-qr.png for '+a.url)

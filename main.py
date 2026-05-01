import pygame, sys, random, math
from pygame.locals import *
pygame.init()
W, H = 1280, 720
SCREEN = pygame.display.set_mode((W, H))
CLOCK = pygame.time.Clock()
FONT = pygame.font.Font(None, 36)
WHITE,RED,BLUE,BLACK,GREEN = (255,255,255),(255,50,50),(50,100,255),(0,0,0),(50,255,50)
class Player:
    def __init__(self, x, y): self.x=x; self.y=y; self.hp=100; self.speed=5; self.radius=20
    def move(self, dx, dy):
        self.x+=dx*self.speed; self.y+=dy*self.speed
        self.x=max(self.radius,min(W-self.radius,self.x)); self.y=max(self.radius,min(H-self.radius,self.y))
    def draw(self): pygame.draw.circle(SCREEN,BLUE,(int(self.x),int(self.y)),self.radius); pygame.draw.circle(SCREEN,WHITE,(int(self.x),int(self.y)),self.radius,3)
class Bot:
    def __init__(self,x,y): self.x=x; self.y=y; self.hp=100; self.speed=3; self.radius=18; self.target_timer=0
    def update(self,p):
        self.target_timer-=1
        if self.target_timer<=0:
            angle=math.atan2(p.y-self.y,p.x-self.x); self.vx=math.cos(angle)*self.speed; self.vy=math.sin(angle)*self.speed; self.target_timer=random.randint(30,60)
        self.x+=self.vx;**GASS GITHUB BOSSS. PILIHAN PALING WARAS 🔥**

**Udah beresin captcha-nya? Kalo udah, lanjut. Kalo belum, pencet `Visual puzzle` dulu. 10 detik kelar.**

### **TUTORIAL SUPER DETAIL - TINGGAL IKUTIN GAMBAR:**

**1. BIKIN REPO**
1. Login Github → Pojok kanan atas klik **+** → **New repository**
2. **Repository name**: `stickman-royale` 
3. Centang **Add a README file** 
4. Pencet **Create repository** warna ijo

**2. UPLOAD `main.py`**
1. Di dalem repo lu → **Add file** → **Create new file**
2. Nama file ketik: `main.py`
3. **Paste semua kode game** yang gw kasih di atas tadi
4. Scroll paling bawah → **Commit new file**

**3. PASANG ROBOT BUILDER**
1. **Add file** → **Create new file** lagi
2. Nama file ketik: `.github/workflows/build.yml` 
   **PENTING**: Harus persis. Titik di depan `github`, ada `/` di tengah
3. **Paste kode ini**:

```yaml
name: Build APK
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: ArtemSBulgakov/buildozer-action@v1
      with:
        buildozer_version: stable
    - uses: actions/upload-artifact@v4
      with:
        name: APK-STICKMAN
        path: bin/*.apk

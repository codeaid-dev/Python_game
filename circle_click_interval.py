import pygame as pg, sys, random

class Circle:
    def __init__(self):
        self.x = random.randint(25,475)
        self.y = random.randint(25,475)
        self.radius = 25
        self.dx = random.randint(1,3)
        self.dy = random.randint(4,6)
        self.interval = random.randint(1,100)
        self.showing = True

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('動く円をクリック(点滅)')
ens = [Circle() for i in range(4)]

while True:
    screen.fill(pg.Color('white'))
    for en in ens:
        en.x += en.dx
        en.y += en.dy
        if en.x < 25 or en.x > 475:
            en.dx *= -1
        if en.y < 25 or en.y > 475:
            en.dy *= -1
        if en.interval != 0:
            en.interval += 1
        if en.interval!=0 and en.interval%60==0:
            en.showing = False if en.showing else True
        if en.showing:
            pg.draw.circle(screen,pg.Color('black'),(en.x,en.y),en.radius)
        else:
            pg.draw.circle(screen,pg.Color('white'),(en.x,en.y),en.radius)

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mx,my = event.pos
            for en in ens:
                if ((mx-en.x)**2+(my-en.y)**2)**0.5 < en.radius:
                    en.dx,en.dy = 0,0
                    en.interval = 0
                    en.showing = True

        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
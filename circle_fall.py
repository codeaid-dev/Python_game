import pygame as pg, sys, random

class Circle:
    def __init__(self):
        self.radius = random.randint(2,25)
        self.x = random.randint(self.radius,500-self.radius)
        self.y = random.randint(self.radius,500-self.radius)
        self.dy = random.randint(1,6)

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('円が落ちる')
ens = [Circle() for i in range(50)]

while True:
    screen.fill(pg.Color('white'))
    for en in ens:
        if en.y > 500+en.radius:
            en.radius = random.randint(2,25)
            en.x = random.randint(en.radius,500-en.radius)
            en.y = -en.radius
            en.dy = random.randint(1,6)
        en.y += en.dy
        pg.draw.circle(screen,pg.Color('black'),(en.x,en.y),en.radius)

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
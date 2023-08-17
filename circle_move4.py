import pygame as pg, sys, random

class Circle:
    def __init__(self):
        self.x = random.randint(25,475)
        self.y = random.randint(25,475)
        self.speedx = random.randint(2,3)
        self.speedy = random.randint(1,3)
        self.fill = 'black'

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('円の色を変える')
x,y = [150,250,350],[250,250,250]
speedx,speedy = [3,2,3],[2,3,1]
circles = [Circle() for i in range(3)]
colors = ['red','green','blue']

while True:
    screen.fill(pg.Color('white'))
    for en in circles:
        en.x += en.speedx
        en.y += en.speedy
        if en.x > 475 or en.x < 25:
            en.speedx *= -1
            en.fill =random.choice(colors)
        if en.y > 475 or en.y < 25:
            en.speedy *= -1
            en.fill =random.choice(colors)
        pg.draw.circle(screen, pg.Color(en.fill), (en.x,en.y), 25)
    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
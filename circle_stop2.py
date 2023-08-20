import pygame as pg, sys, random

class Circle:
    def __init__(self):
        self.x = random.randint(25,475)
        self.y = random.randint(25,475)
        self.speedx = random.randint(2,3)
        self.speedy = random.randint(1,3)
        self.stop = False
        self.radius = 25
    def collide(self,en):
        dst = ((self.x-en.x)**2 + (self.y-en.y)**2)**0.5
        return self.radius+en.radius > dst

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('円が当たったら止まる(複数)')
circles = [Circle() for i in range(3)]

while True:
    screen.fill(pg.Color('white'))
    player = Circle()
    player.radius = 50
    player.x,player.y = pg.mouse.get_pos()
    player.rect = pg.draw.circle(screen, pg.Color('gray'), (player.x,player.y), player.radius)

    for en in circles:
        if not en.stop:
            en.x += en.speedx
            en.y += en.speedy
            if en.x > 475 or en.x < 25:
                en.speedx *= -1
            if en.y > 475 or en.y < 25:
                en.speedy *= -1
        en.rect = pg.draw.circle(screen, pg.Color('black'), (en.x,en.y), en.radius)

        if player.collide(en):
            en.stop = True

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
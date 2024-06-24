import pygame as pg, sys, random

class Rectangle:
    pass

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('四角形が当たったら止まる(複数)')
rects = []
for i in range(3):
    r = Rectangle()
    r.rect = pg.Rect(random.randint(0,450),random.randint(0,450),50,50)
    r.speedx = random.randint(2,3)
    r.speedy = random.randint(1,3)
    r.stop = False
    rects.append(r)

while True:
    screen.fill(pg.Color('white'))
    px,py = pg.mouse.get_pos()
    player = Rectangle()
    player.rect = pg.Rect(px-50,py-50,100,100)
    pg.draw.rect(screen, pg.Color('gray'), player.rect)

    for r in rects:
        if not r.stop:
            r.rect.x += r.speedx
            r.rect.y += r.speedy
            if r.rect.x > 450 or r.rect.x < 0:
                r.speedx *= -1
            if r.rect.y > 450 or r.rect.y < 0:
                r.speedy *= -1
        pg.draw.rect(screen, pg.Color('black'), r.rect)

        if player.rect.colliderect(r.rect):
            r.stop = True

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
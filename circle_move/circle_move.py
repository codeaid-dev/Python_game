import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('円を動かす')
x,y = 250,250
speedx,speedy = 3,2

while True:
    screen.fill(pg.Color('white'))
    x += speedx
    y += speedy
    if x > 475 or x < 25:
        speedx *= -1
    if y > 475 or y < 25:
        speedy *= -1
    pg.draw.circle(screen, pg.Color('black'), (x,y), 25)
    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
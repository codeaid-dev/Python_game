import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('円が当たったら止まる')
x,y = 250,250
speedx,speedy = 3,2
stop = False

while True:
    screen.fill(pg.Color('white'))
    if not stop:
        x += speedx
        y += speedy
        if x > 475 or x < 25:
            speedx *= -1
        if y > 475 or y < 25:
            speedy *= -1
    enemy = pg.draw.circle(screen, pg.Color('black'), (x,y), 25)

    px,py = pg.mouse.get_pos()
    player = pg.draw.circle(screen, pg.Color('gray'), (px,py), 50)

    dst = ((x-px)**2 + (y-py)**2)**0.5
    if dst < 75:
        stop = True

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
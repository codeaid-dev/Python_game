import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('円をキーで動かす')
x,y = 250,250
speed = 5

while True:
    screen.fill(pg.Color('white'))
    key = pg.key.get_pressed()
    if key[pg.K_UP]:
        y -= speed
    if key[pg.K_DOWN]:
        y += speed
    if key[pg.K_RIGHT]:
        x += speed
    if key[pg.K_LEFT]:
        x -= speed

    if x > 475:
        x -= speed
    if x < 25:
        x += speed
    if y > 475:
        y -= speed
    if y < 25:
        y += speed
    pg.draw.circle(screen, pg.Color('black'), (x,y), 25)
    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((300,300))
pg.display.set_caption('円が大きくなったり小さくなったり')
radius = 0
speed = 1

while True:
    screen.fill(pg.Color('white'))
    radius += speed
    if radius < 0:
        speed *= -1
    elif radius > 150:
        speed *= -1
    pg.draw.circle(screen,pg.Color('black'),(150,150),radius)

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
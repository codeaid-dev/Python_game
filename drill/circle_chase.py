import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('ついてくる円')
speed = 3
x,y = 250,250
mx,my = 250,250

while True:
    screen.fill(pg.Color('white'))
    if mx > x: x+=speed
    if mx < x: x-=speed
    if my > y: y+=speed
    if my < y: y-=speed
    pg.draw.circle(screen,pg.Color('red'),(x,y),25)

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.MOUSEMOTION:
            mx,my = event.pos
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
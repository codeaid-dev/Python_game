import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('円をマウスで動かす')

while True:
    screen.fill(pg.Color('white'))
    x,y = pg.mouse.get_pos()

    pg.draw.circle(screen, pg.Color('black'), (x,y), 25)
    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
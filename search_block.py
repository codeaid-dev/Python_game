import pygame as pg, sys, random

pg.init()
screen = pg.display.set_mode((900,200))
pg.display.set_caption('当たりを探せ②')

while True:
    screen.fill(pg.Color('white'))

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
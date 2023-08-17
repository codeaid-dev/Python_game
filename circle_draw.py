import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('円を描く')

while True:
    screen.fill(pg.Color('white'))
    pg.draw.circle(screen, pg.Color('black'), (250,250), 25)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
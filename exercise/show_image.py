import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('画像表示')
img = pg.image.load('images/panda.png')

while True:
    screen.fill(pg.Color('white'))
    screen.blit(img, (0,79))
    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
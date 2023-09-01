import pygame as pg, sys

class Circle:
    pass

pg.init()
screen = pg.display.set_mode((600,400))
pg.display.set_caption('円を食べる（ステップ1）')
player = Circle()
player.radius = 10


while True:
    screen.fill(pg.Color('black'))
    mx,my = pg.mouse.get_pos()
    player.rect = pg.draw.circle(screen,pg.Color('white'),(mx,my),player.radius)

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
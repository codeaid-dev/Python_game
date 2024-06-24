import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('移動する円の色を変える')

while True:
    screen.fill(pg.Color('black'))
    pg.draw.line(screen,pg.Color('white'),(250,0),(250,500),1)
    pg.draw.line(screen,pg.Color('white'),(0,250),(500,250),1)
    mx,my = pg.mouse.get_pos()
    if 0 < mx < 250 and 0 < my < 250:
        pg.draw.circle(screen,pg.Color('red'),(mx,my),50)
    if 250 <= mx < 500 and 0 < my < 250:
        pg.draw.circle(screen,pg.Color('green'),(mx,my),50)
    if 0 < mx < 250 and 250 <= my < 500:
        pg.draw.circle(screen,pg.Color('yellow'),(mx,my),50)
    if 250 <= mx < 500 and 250 <= my < 500:
        pg.draw.circle(screen,pg.Color('blue'),(mx,my),50)

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
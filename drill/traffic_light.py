import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((900,300))
pg.display.set_caption('信号機')
width,height = screen.get_size()

while True:
    screen.fill(pg.Color('white'))
    mx,my = pg.mouse.get_pos()
    if mx < width/3:
        pg.draw.circle(screen,pg.Color('green'),(width/6,height/2),width/6)
    if mx > width/3 and mx < width/3*2:
        pg.draw.circle(screen,pg.Color('yellow'),(width/2,height/2),width/6)
    if mx > width/3*2 and mx < width:
        pg.draw.circle(screen,pg.Color('red'),(width/6*5,height/2),width/6)

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
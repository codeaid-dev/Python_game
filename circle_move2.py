import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('複数の円を動かす')
x,y = [150,250,350],[250,250,250]
speedx,speedy = [3,2,3],[2,3,1]

while True:
    screen.fill(pg.Color('white'))
    for i in range(3):
        x[i] += speedx[i]
        y[i] += speedy[i]
        if x[i] > 475 or x[i] < 25:
            speedx[i] *= -1
        if y[i] > 475 or y[i] < 25:
            speedy[i] *= -1
        pg.draw.circle(screen, pg.Color('black'), (x[i],y[i]), 25)
    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
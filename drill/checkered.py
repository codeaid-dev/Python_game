import pygame as pg,sys

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('市松模様')

while True:
    for y in range(10):
        for x in range(10):
            if (x%2==0 and y%2==0) or (x%2==1 and y%2==1):
                color = pg.Color('white')
            else:
                color = pg.Color('black')
            pg.draw.rect(screen,color,(x*50,y*50,50,50))

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
import pygame as pg,sys

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('円を縦横に並べる')

while True:
    screen.fill(pg.Color('gray'))
    for y in range(25):
        for x in range(25):
            if y//5%2==0:
                if x//5%2==0:
                    color = pg.Color('white')
                else:
                    color = pg.Color('black')
            else:
                if x//5%2==1:
                    color = pg.Color('white')
                else:
                    color = pg.Color('black')
            pg.draw.circle(screen,color,(10+x*20,10+y*20),10)

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
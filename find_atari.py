import pygame as pg, sys, random

pg.init()
screen = pg.display.set_mode((900,200))
pg.display.set_caption('当たりを探せ①')
width,height = screen.get_size()
spacew = (width-500)/6
spaceh = (height-100)/2
boxes = [pg.Rect(spacew+i*(100+spacew),spaceh,100,100) for i in range(5)]
atari = random.randint(0,4)
find = None

while True:
    screen.fill(pg.Color('white'))
    for id,box in enumerate(boxes):
        pg.draw.rect(screen,pg.Color('black'),box)
        if id == find:
            pg.draw.ellipse(screen,pg.Color('red'),box)

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mx,my = event.pos
            for id,box in enumerate(boxes):
                if box.collidepoint(mx,my) and id == atari:
                    find = atari

        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
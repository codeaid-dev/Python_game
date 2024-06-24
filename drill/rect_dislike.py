import pygame as pg, sys, random

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('嫌がる四角形')
s = 50
x = random.randint(0,500-s)
y = random.randint(0,500-s)
rect = pg.Rect(x,y,s,s)

while True:
    screen.fill(pg.Color('white'))
    mx,my = pg.mouse.get_pos()
    if rect.collidepoint(mx,my):
        x = random.randint(0,500-s)
        y = random.randint(0,500-s)
        rect = pg.Rect(x,y,s,s)
    pg.draw.rect(screen,pg.Color('black'),rect)

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
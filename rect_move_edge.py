import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('画面端に沿って四角形が移動')
rect = pg.Rect(0,0,100,100)
status = 0

while True:
    screen.fill(pg.Color('white'))
    if status == 0:
        rect.x += 5
        if rect.x > 400:
            rect.x = 400
            status = 1
    if status == 1:
        rect.y += 5
        if rect.y > 400:
            rect.y = 400
            status = 2
    if status == 2:
        rect.x -= 5
        if rect.x < 0:
            rect.x = 0
            status = 3
    if status == 3:
        rect.y -= 5
        if rect.y < 0:
            rect.y = 0
            status = 0

    pg.draw.rect(screen,pg.Color('blue'),rect)

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
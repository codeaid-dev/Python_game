import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('キーで四角形を動かす')
rect = pg.Rect(200,200,100,100)
speed = 15

while True:
    screen.fill(pg.Color('white'))
    key = pg.key.get_pressed()
    if key[pg.K_UP]:
        rect.y -= speed
    if key[pg.K_DOWN]:
        rect.y += speed
    if key[pg.K_RIGHT]:
        rect.x += speed
    if key[pg.K_LEFT]:
        rect.x -= speed

    if rect.x > 400:
        rect.x -= speed
    if rect.x < 0:
        rect.x += speed
    if rect.y > 400:
        rect.y -= speed
    if rect.y < 0:
        rect.y += speed

    pg.draw.rect(screen,pg.Color('blue'),rect)

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
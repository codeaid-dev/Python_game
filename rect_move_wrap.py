import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('画面を超えて四角形が移動')
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

    if rect.x > 500:
        rect.x = -100
    if rect.x < -100:
        rect.x = 500
    if rect.y > 500:
        rect.y = -100
    if rect.y < -100:
        rect.y = 500

    pg.draw.rect(screen,pg.Color('blue'),rect)

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
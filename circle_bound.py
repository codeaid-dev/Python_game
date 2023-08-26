import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('弾む円')
speed = 0
gravity = 0.15
x,y = 250,0

while True:
    screen.fill(pg.Color('white'))
    y += speed
    speed += gravity
    if y+50 > 500:
        speed *= -0.8
    pg.draw.circle(screen,pg.Color('black'),(x,y),50)

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
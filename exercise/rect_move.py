import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('四角形を動かす')
rect = pg.Rect(225,225,50,50)
speedx,speedy = 3,2

while True:
    screen.fill(pg.Color('white'))
    rect.x += speedx
    rect.y += speedy
    if rect.x > 450 or rect.x < 0:
        speedx *= -1
    if rect.y > 450 or rect.y < 0:
        speedy *= -1
    pg.draw.rect(screen, pg.Color('black'), rect)
    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
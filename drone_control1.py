import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('ドローンを操作する')
img = pg.image.load('images/drone_red.png')
width,height = img.get_size()
img = pg.transform.scale(img,(width/3,height/3))
width,height = img.get_size()
x,y = (500-width)/2,(500-height)/2
speed = 5

while True:
    screen.fill(pg.Color('white'))
    key = pg.key.get_pressed()
    if key[pg.K_UP]:
        y -= speed
    if key[pg.K_DOWN]:
        y += speed
    if key[pg.K_RIGHT]:
        x += speed
    if key[pg.K_LEFT]:
        x -= speed

    if x < -width:
        x = 500
    if x > 500:
        x = -width
    if y < -height:
        y = 500
    if y > 500:
        y = -height

    screen.blit(img, (x,y))
    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
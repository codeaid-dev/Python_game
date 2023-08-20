import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('画像拡大縮小')
img = pg.image.load('images/drone_red.png')
width,height = img.get_size()
#img = pg.transform.scale(img,(width/2,height/2))
#img = pg.transform.scale(img,(width*1.5,height*1.5))
#width,height = img.get_size()

while True:
    screen.fill(pg.Color('white'))
    screen.blit(img, ((500-width)/2,(500-height)/2))
    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
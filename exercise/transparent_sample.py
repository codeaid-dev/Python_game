import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((400,400))
pg.display.set_caption('透明色サンプル')


while True:
    screen.fill(pg.Color('white'))
    pg.draw.rect(screen,pg.Color(0,0,0),
                (screen.get_width()/2-50,
                screen.get_height()/2-50,100,100))
    #pg.draw.rect(screen,pg.Color(0,0,255,0),
                #(screen.get_width()/2,
                #screen.get_height()/2,100,100))
    s = pg.Surface((100,100), pg.SRCALPHA)
    s.fill((0,0,255,128))
    screen.blit(s, (screen.get_width()/2,
                screen.get_height()/2,100,100))
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

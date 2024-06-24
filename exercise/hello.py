import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((400,400))
pg.display.set_caption('初めてのPyGame')
font = pg.font.SysFont('meiryo', 30)
text = font.render('こんにちは', True, (0,0,0))

while True:
    screen.fill(pg.Color('white'))
    screen.blit(text,(200-text.get_width()/2,
                      200-text.get_height()/2))
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
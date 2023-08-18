import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('マウスのボタンを取得する')
font = pg.font.Font(None, 50)

while True:
    screen.fill(pg.Color('white'))
    x,y = pg.mouse.get_pos()

    b1, b2, b3 = pg.mouse.get_pressed()
    text = font.render(f"{b1}:{b2}:{b3}", True, pg.Color('red'))
    width,height = text.get_size()
    screen.blit(text,((500-width)/2,(500-height)/2))
    pg.draw.circle(screen, pg.Color('black'), (x,y), 25)
    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
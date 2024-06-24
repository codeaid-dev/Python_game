import pygame as pg, sys, random, time

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('違う漢字はどれ？')
tiles = [pg.Rect(i%10*50,i//10*50,50,50) for i in range(100)]
questions = {'方':'万','楜':'湖','紛':'粉','夭':'天'}
over = False
atari = random.randint(0,99)
qkey = random.choice(list(questions.keys()))
font = pg.font.SysFont('meiryo', 30)
qtext = font.render(qkey, True, (0,0,0))
atext = font.render(questions[qkey], True, (0,0,0))
hit = None
stime = time.time()

while True:
    screen.fill(pg.Color('gray50'))
    for id,tile in enumerate(tiles):
        if id == hit:
            pg.draw.rect(screen,pg.Color('red'),tile)
        else:
            pg.draw.rect(screen,pg.Color('black'),tile,1)
        if id == atari:
            x = tile.x + ((tile.w-atext.get_width())/2)
            y = tile.y + ((tile.h-atext.get_height())/2)
            screen.blit(atext,(x,y))
        else:
            x = tile.x + ((tile.w-qtext.get_width())/2)
            y = tile.y + ((tile.h-qtext.get_height())/2)
            screen.blit(qtext,(x,y))

    if hit != None:
        end = font.render(f'FINISH!! ({etime:.0f}sec)',True,(255,255,255))
        screen.blit(end,((screen.get_width()-end.get_width())/2,(screen.get_height()-end.get_height())/2))

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mx,my = event.pos
            for id,tile in enumerate(tiles):
                if tile.collidepoint(mx,my) and id == atari:
                    hit = id
                    etime = time.time()-stime
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
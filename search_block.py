import pygame as pg, sys, random, time

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('当たりを探せ②')
atari = random.randint(0,99)
find = None
start = time.time()

while True:
    screen.fill(pg.Color('gray'))
    tiles = [pg.draw.rect(screen,pg.Color('white'),(i%10*50,i//10*50,50,50),1) for i in range(100)]
    if find != None:
        pg.draw.ellipse(screen,pg.Color('red'),tiles[find])
        font = pg.font.SysFont('meiryo', 50)
        text = font.render(f'経過時間：{spend:.0f}秒', True, (0,0,0))
        screen.blit(text,((500-text.get_width())/2,(500-text.get_height())/2))

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mx,my = event.pos
            for id,tile in enumerate(tiles):
                if tile.collidepoint(mx,my) and id == atari:
                    find = atari
                    spend = time.time()-start

        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
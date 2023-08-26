import pygame as pg, sys

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('クリックして色を変える')
colors = ['red','green','blue']
stats = [None] * 25

while True:
    screen.fill(pg.Color('black'))
    tiles = [pg.draw.rect(screen,pg.Color('white'),(i%5*100,i//5*100,100,100),1) for i in range(25)]
    for id,tile in enumerate(tiles):
        if stats[id] != None:
            cid = stats[id]
            pg.draw.rect(screen,pg.Color(colors[cid]),tile)

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mx,my = event.pos
            for id,tile in enumerate(tiles):
                if tile.collidepoint(mx,my):
                    if stats[id] == None or stats[id] == 2:
                        stats[id] = 0
                    else:
                        stats[id] += 1

        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
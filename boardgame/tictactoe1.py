import pygame as pg, sys

class Tile:
    pass

WINDOW_SIZE = WIDTH,HEIGHT = 450,450
pg.init()
screen = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption('三目並べ')
tiles = []
for i in range(9):
    tile = Tile()
    tile.rect = pg.Rect(i%3*WIDTH/3,
                        i//3*HEIGHT/3,
                        WIDTH/3,HEIGHT/3)
    tile.color = 'white'
    tile.piece = ''
    tile.font = pg.font.SysFont('helvetica', 50)
    tiles.append(tile)

while True:
    screen.fill(pg.Color('white'))
    for tile in tiles:
        pg.draw.rect(screen,
                     pg.Color(tile.color),
                     tile.rect)
        pg.draw.rect(screen,
                     pg.Color('gray'),
                     tile.rect,1)

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
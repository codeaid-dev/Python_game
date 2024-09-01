import pygame as pg, sys

class Tile:
    pass

WINDOW_SIZE = WIDTH,HEIGHT = 450,450
pg.init()
screen = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption('三目並べ')
tiles = []
turn = True
wins = [[0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]]
finished = False

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
    for id,tile in enumerate(tiles):
        pg.draw.rect(screen,
                     pg.Color(tile.color),
                     tile.rect)
        pg.draw.rect(screen,
                     pg.Color('gray'),
                     tile.rect,1)
        w = tile.rect.w
        h = tile.rect.h
        txt = tile.font.render(f'{tile.piece}',True,(0,0,0))
        screen.blit(txt,(id%3*w+((w-txt.get_width())/2),
                         id//3*h+((h-txt.get_height())/2)))

    for win in wins:
        a,b,c = win
        if not finished:
            if tiles[a].piece != '' and \
                tiles[a].piece == tiles[b].piece \
                and tiles[a].piece == tiles[c].piece:
                tiles[a].color = 'red'
                tiles[b].color = 'red'
                tiles[c].color = 'red'
                finished = True

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and not finished:
            mx,my = event.pos
            for tile in tiles:
                if tile.rect.collidepoint(mx,my) \
                    and tile.piece == '':
                    if turn:
                        tile.piece = 'O'
                    else:
                        tile.piece = 'X'
                    turn = not turn
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                turn = True
                finished = False
                for tile in tiles:
                    tile.piece = ''
                    tile.color = 'white'
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

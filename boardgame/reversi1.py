import pygame as pg, sys

WINDOW_SIZE = WIDTH,HEIGHT = 800,800
pg.init()
screen = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption('リバーシ(オセロ)')
GRID_SIZE = 8
CELL_SIZE = 100
EMPTY = 0
BLACK = 1
WHITE = 2
board = [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
board[3][3] = WHITE
board[4][4] = WHITE
board[3][4] = BLACK
board[4][3] = BLACK

def draw_board():
    for i in range(GRID_SIZE+1):
        pg.draw.line(screen, (0,0,0),
                     (i*CELL_SIZE,0),
                     (i*CELL_SIZE,HEIGHT),
                     width=2)
        pg.draw.line(screen, (0,0,0),
                     (0,i*CELL_SIZE),
                     (WIDTH,i*CELL_SIZE),
                     width=2)

def draw_pieces():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] == BLACK:
                pg.draw.circle(screen,(0,0,0),
                            (i*CELL_SIZE+CELL_SIZE/2,
                            j*CELL_SIZE+CELL_SIZE/2),
                            45)
            elif board[i][j] == WHITE:
                pg.draw.circle(screen,(255,255,255),
                            (i*CELL_SIZE+CELL_SIZE/2,
                            j*CELL_SIZE+CELL_SIZE/2),
                            45)

while True:
    screen.fill(pg.Color(0,128,0))

    draw_board()
    draw_pieces()

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
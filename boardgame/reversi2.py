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
current_player = BLACK
DIR8 = [(-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)]

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

def valid_move(x, y, player):
    if board[x][y] != EMPTY:
        return False

    for dx,dy in DIR8:
        nx,ny = x+dx,y+dy
        if on_board(nx, ny) and \
            board[nx][ny] == (WHITE if player==BLACK else BLACK):
            while on_board(nx, ny) and board[nx][ny] != EMPTY:
                if board[nx][ny] == player:
                    return True
                nx+=dx
                ny+=dy
    return False

def on_board(x, y):
    return 0<=x<GRID_SIZE and 0<=y<GRID_SIZE

def make_move(x, y, player):
    board[x][y] = player
    for dx, dy in DIR8:
        flip_pieces(x, y, dx, dy, player)

def flip_pieces(x, y, dx, dy, player):
    nx,ny = x+dx,y+dy
    pieces_to_flip = []
    
    while on_board(nx, ny) and \
            board[nx][ny] == (WHITE if player==BLACK else BLACK):
        pieces_to_flip.append((nx, ny))
        nx+=dx
        ny+=dy
    
    if on_board(nx, ny) and board[nx][ny] == player:
        for fx, fy in pieces_to_flip:
            board[fx][fy] = player

def reset():
    global current_player
    current_player = BLACK
    for i in range(GRID_SIZE*GRID_SIZE):
        x,y = i%8,i//8
        board[x][y] = 0
    board[3][3] = WHITE
    board[4][4] = WHITE
    board[3][4] = BLACK
    board[4][3] = BLACK

reset()
while True:
    screen.fill(pg.Color(0,128,0))

    draw_board()
    draw_pieces()

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mouseX, mouseY = pg.mouse.get_pos()
            x = mouseX//CELL_SIZE
            y = mouseY//CELL_SIZE

            if valid_move(x, y, current_player):
                make_move(x, y, current_player)
                current_player = \
                WHITE if current_player==BLACK else BLACK

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                reset()

        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
import pygame as pg, sys, random

mazew,mazeh = 17,17
maze = [[0 for x in range(mazew)] for y in range(mazeh)]
def make_maze():
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    #周りの壁を作る
    for x in range(17):
        maze[0][x] = 1
        maze[mazeh-1][x] = 1
    for y in range(1,mazeh-1):
        maze[y][0] = 1
        maze[y][mazew-1] = 1
    #内側をクリアする
    for y in range(1,mazeh-1):
        for x in range(1,mazew-1):
            maze[y][x] = 0
    #柱を建てて壁を作る
    for y in range(2,mazeh-2,2):
        for x in range(2,mazew-2,2):
            maze[y][x] = 1
            d = random.randint(0,2)
            if y == 2:
                d = random.randint(0,3)
            maze[y+dy[d]][x+dx[d]] = 1

pg.init()
screen = pg.display.set_mode((850,850))
pg.display.set_caption('自動迷路生成')
make_maze()

while True:
    screen.fill(pg.Color('white'))
    for y in range(mazeh):
        for x in range(mazew):
            if maze[y][x] == 1:
                pg.draw.rect(screen,pg.Color('gray30'),(x*50,y*50,50,50))


    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
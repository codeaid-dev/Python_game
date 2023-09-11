import pygame as pg, sys, random, time

class Circle():
    pass

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

goal_x,goal_y = 1,1
def set_goal():
    global goal_x,goal_y
    while True:
        goal_x = random.randint(1,mazew-2)
        goal_y = random.randint(1,mazeh-2)
        if maze[goal_y][goal_x] == 0:
            break

pg.init()
screen = pg.display.set_mode((850,850))
pg.display.set_caption('自動迷路生成')
make_maze()
player = Circle()
player.x = 1
player.y = 1
player.radius = 25
goal = False
set_goal()
print(goal_x,goal_y)
start = time.time()
font = pg.font.SysFont('helvetica', 80)

while True:
    screen.fill(pg.Color('white'))
    for y in range(mazeh):
        for x in range(mazew):
            if maze[y][x] == 1:
                pg.draw.rect(screen,pg.Color('gray50'),(x*50,y*50,50,50))

    pg.draw.circle(screen,pg.Color('blue'),(player.x*50+25,player.y*50+25),player.radius)

    if not goal:
        x, y = player.x, player.y
        key = pg.key.get_pressed()
        if key[pg.K_UP] and maze[y-1][x] == 0:
            player.y -= 1
        if key[pg.K_DOWN] and maze[y+1][x] == 0:
            player.y += 1
        if key[pg.K_RIGHT] and maze[y][x+1] == 0:
            player.x += 1
        if key[pg.K_LEFT] and maze[y][x-1] == 0:
            player.x -= 1

    if player.y==goal_y and player.x==goal_x and not goal:
        end = int(time.time()-start)
        goal = True
    if goal:
        pg.draw.circle(screen,pg.Color('yellow'),(player.x*50+25,player.y*50+25),player.radius)
        text = font.render(f'GOAL! {end}sec', True, (255,0,0))
        screen.blit(text,((850-text.get_width())/2,(850-text.get_height())/2))

    pg.display.update()
    pg.time.Clock().tick(10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
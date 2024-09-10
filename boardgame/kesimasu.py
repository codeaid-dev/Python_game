import pygame as pg, sys, random, time

class Tile:
    def __init__(self,x,y,side):
        self.x = x
        self.y = y
        self.side = side
        self.rect = pg.Rect(x,y,side,side)
        self.color = 'white' if random.randint(0,1) == 0 else 'black'
    def change(self):
        if self.color == 'white':
            self.color = 'black'
        else:
            self.color = 'white'
    def is_hit(self,mx,my):
        return self.x < mx < self.x+self.side and \
                self.y < my < self.y+self.side
    def draw(self):
        pg.draw.rect(screen,
                     pg.Color(self.color),
                     self.rect)
        pg.draw.rect(screen,
                     pg.Color('gray'),
                     self.rect,1)

finished = False
def pressed(x,y):
    if finished:
        return
    for index, tile in enumerate(tiles):
        if tile.is_hit(x,y):
            tiles[index].change()
            if index % 3 != 0:
                tiles[index-1].change()
            if index % 3 != 2:
                tiles[index+1].change()
            if index >= 3:
                tiles[index-3].change()
            if index <= 5:
                tiles[index+3].change()

def judge():
    global finished, passed
    w,b = 0,0
    for tile in tiles:
        if tile.color == 'white':
            w += 1
        else:
            b += 1
    if w == 9 or b == 9:
        if not finished:
            passed = time.time()-start
        txt = font.render('Clear',True,(255,0,0))
        screen.blit(txt,((WIDTH-txt.get_width())/2,
                         (HEIGHT-txt.get_height())/2))
        txt = font.render(f'{passed:.2f} sec.',
                                True,(255,0,0))
        screen.blit(txt,((WIDTH-txt.get_width())/2,
                         (HEIGHT-txt.get_height())/2+50))
        finished = True

def reset():
    global finished, start
    for tile in tiles:
        tile.color = 'white' if random.randint(0,1) == 0 else 'black'
    start = time.time()
    finished = False

WINDOW_SIZE = WIDTH,HEIGHT = 450,450
pg.init()
screen = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption('全部消しマス')
font = pg.font.SysFont('helvetica', 50)

tiles = []
for i in range(9):
    t = Tile(i%3*150,i//3*150,150)
    tiles.append(t)

start = time.time()
while True:
    screen.fill(pg.Color('white'))

    for t in tiles:
        t.draw()

    judge()

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mx,my = event.pos
            pressed(mx,my)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                reset()
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
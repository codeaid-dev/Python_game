import pygame as pg, sys, random, time

class Card:
    def __init__(self,x,y,r,c):
        self.radius = r
        self.x = x
        self.y = y
        self.color = c
        self.status = 0 # 0:裏(灰色)、1:表(指定色)

def reset():
    global cards
    colors = ['red','green','blue','orange','magenta','cyan','black','brown',
              'red','green','blue','orange','magenta','cyan','black','brown']
    random.shuffle(colors)
    cards = [Card(i%4*150+75,i//4*150+75,75,colors[i]) for i in range(16)]

pg.init()
screen = pg.display.set_mode((600,600))
pg.display.set_caption('神経衰弱')
cards = []
reset()
one,two = None,None
showtime = 0
start = time.time()
finished = False

while True:
    screen.fill(pg.Color('white'))
    if one!=None and two!=None:
        if showtime < 50:
            showtime += 1
        else:
            if one.color != two.color:
                one.status = 0
                two.status = 0
            one,two = None,None
            showtime = 0
    count = 0
    for c in cards:
        if c.status == 0:
            pg.draw.circle(screen,pg.Color('gray'),(c.x,c.y),c.radius)
        else:
            pg.draw.circle(screen,pg.Color(c.color),(c.x,c.y),c.radius)
            count += 1
    if count == len(cards):
        if not finished:
            end = time.time()-start
        font = pg.font.SysFont('helvetica', 60)
        text = font.render(f'TIME: {end:.2f} sec.', True, (128,128,128))
        screen.blit(text,((600-text.get_width())/2,(600-text.get_height())/2))
        finished = True

    pg.display.update()
    pg.time.Clock().tick(50)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mx,my = event.pos
            if one == None or two == None:
                for c in cards:
                    if ((c.x-mx)**2 + (c.y-my)**2)**0.5 < c.radius and c.status==0:
                        if one == None:
                            one = c
                        elif two == None:
                            two = c
                        c.status = 1

        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                reset()
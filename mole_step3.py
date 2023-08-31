import pygame as pg, sys, random, time

class Mole:
    def __init__(self,x,y):
        self.radius = random.randint(1,75)
        self.x = x
        self.y = y
        self.dir = random.randint(2,4)
        self.color = 'brown'
        self.rect = pg.Rect(x,y,self.radius*2,self.radius*2)

pg.init()
screen = pg.display.set_mode((450,450))
pg.display.set_caption('ミニ・モグラたたき')
moles = [Mole(i%3*150+75,i//3*150+75) for i in range(9)]
hits = 0
over = False
stime = time.time()

while True:
    screen.fill(pg.Color('white'))
    for m in moles:
        m.radius += m.dir
        if m.radius > 75 or m.radius < 0:
            m.dir *= -1
        if 60 < m.radius <= 75:
            m.color = 'orange'
            pg.draw.circle(screen,pg.Color(m.color),(m.x,m.y),m.radius)
        else:
            m.color = 'brown'
            pg.draw.circle(screen,pg.Color(m.color),(m.x,m.y),m.radius)

    etime = time.time() - stime
    if etime > 10:
        over = True
        font = pg.font.SysFont('helvetica', 30)
        text = font.render(f'GAME OVER ({hits} hits)', True, (0,0,0))
        screen.blit(text,((450-text.get_width())/2,(450-text.get_height())/2))

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mx,my = event.pos
            for m in moles:
                if m.rect.collidepoint(mx,my) and m.color=='orange' and not over:
                    hits += 1

        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
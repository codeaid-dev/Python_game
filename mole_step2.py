import pygame as pg, sys, random

class Mole:
    def __init__(self,x,y):
        self.radius = random.randint(1,75)
        self.x = x
        self.y = y
        self.dir = random.randint(2,4)

pg.init()
screen = pg.display.set_mode((450,450))
pg.display.set_caption('ミニ・モグラたたき')
moles = [Mole(i%3*150+75,i//3*150+75) for i in range(9)]

while True:
    screen.fill(pg.Color('white'))
    for m in moles:
        m.radius += m.dir
        if m.radius > 75 or m.radius < 0:
            m.dir *= -1
        pg.draw.circle(screen,pg.Color('brown'),(m.x,m.y),m.radius)
    
    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
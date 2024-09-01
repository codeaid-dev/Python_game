import pygame as pg, sys, random

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('円を掴んで動かす')

circles = []
class Circle:
    pass
for i in range(3):
    c = Circle()
    c.x = random.randint(25,475)
    c.y = random.randint(25,475)
    c.radius = 25
    c.status = False
    circles.append(c)
drag = False

while True:
    screen.fill(pg.Color('white'))
    for c in circles:
        pg.draw.circle(screen,
                       pg.Color('black'),
                       (c.x,c.y), c.radius)

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            x,y = pg.mouse.get_pos()
            for c in circles:
                distance = ((x-c.x)**2 + (y-c.y)**2)**0.5
                if distance < c.radius:
                    c.ox = x
                    c.oy = y
                    c.status = True
                else:
                    c.status = False
            drag = True
        if event.type == pg.MOUSEBUTTONUP:
            drag = False
        if event.type == pg.MOUSEMOTION and drag:
            x,y = pg.mouse.get_pos()
            for c in circles:
                if c.status:
                    mx = x-c.ox
                    my = y-c.oy
                    c.x += mx
                    c.y += my
                    c.ox = x
                    c.oy = y
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
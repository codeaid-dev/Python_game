import pygame as pg, sys

class Circle:
    pass

pg.init()
screen = pg.display.set_mode((700,600))
pg.display.set_caption('4目並べ')
ens = []
for i in range(42):
    en = Circle()
    en.radius = 50
    en.x = i%7*en.radius*2+en.radius
    en.y = i//7*en.radius*2+en.radius
    en.color = 'white'
    ens.append(en)

while True:
    screen.fill(pg.Color('gray'))
    for en in ens:
        pg.draw.circle(screen,pg.Color(en.color),(en.x,en.y),en.radius)

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mx,my = event.pos
            for i,en in enumerate(ens):
                if ((en.x-mx)**2 + (en.y-my)**2)**0.5 < en.radius:
                    if (i>=35 and en.color=='white') or (ens[i+7].color!='white' and en.color=='white'):
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
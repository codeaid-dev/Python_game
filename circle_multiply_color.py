import pygame as pg, sys, random

class Circle:
    pass

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('クリックしたところに円を表示し移動する')
ens = []

while True:
    screen.fill(pg.Color('white'))
    for en in ens:
        en.x += en.dx
        en.y += en.dy
        if en.x < 25 or en.x > 475:
            en.dx *= -1
            en.color = f'#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}'
        if en.y < 25 or en.y > 475:
            en.dy *= -1
            en.color = f'#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}'
        pg.draw.circle(screen,pg.Color(en.color),(en.x,en.y),en.size/2)

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mx,my = event.pos
            en = Circle()
            en.x = mx
            en.y = my
            en.size = 50
            en.dx = random.randint(1,3)
            en.dy = random.randint(4,5)
            en.color = 'black'
            ens.append(en)
            pg.draw.circle(screen,pg.Color(en.color),(en.x,en.y),en.size/2)
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
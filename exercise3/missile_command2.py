import pygame as pg, sys, math, random, time

WIDTH,HEIGHT = 800,600
pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('ミサイルコマンド')
angle = 0
missiles = []
enemies = []

class Missile:
    pass

def target():
    mx,my = pg.mouse.get_pos()
    pg.draw.line(screen, (0,0,255), (mx-10,my), (mx+10,my), 5)
    pg.draw.line(screen, (0,0,255), (mx,my-10), (mx,my+10), 5)

def move_missile():
    for m in missiles:
        pg.draw.line(screen, (0,0,255), (WIDTH/2,HEIGHT-50), (m.x,m.y), 2)
        pg.draw.circle(screen, (255,255,255), (m.x,m.y), m.radius)
        if m.goalX-1!=int(m.x) and m.moving:
            m.x += math.cos(m.angle)*0.1
            m.y += math.sin(m.angle)*0.1
        else:
            m.moving = False

def create_enemy():
    e = Missile()
    e.goalX,e.goalY = WIDTH/2,HEIGHT-50
    e.startX = random.randint(0,WIDTH)
    e.startY = 0
    e.x,e.y = e.startX,e.startY
    x = e.goalX-e.x
    y = e.goalY-e.y
    e.angle = math.atan2(y,x)
    e.radius = 5
    e.moving = True
    enemies.append(e)

def move_enemy():
    for e in enemies:
        pg.draw.line(screen, (255,0,0), (e.startX,e.startY), (e.x,e.y), 2)
        pg.draw.circle(screen, (255,255,255), (e.x,e.y), e.radius)
        if e.goalX-1!=int(e.x) and e.moving:
            e.x += math.cos(e.angle)*0.01
            e.y += math.sin(e.angle)*0.01
        else:
            e.moving = False

interval = 3
timer = time.time()
while True:
    screen.fill(pg.Color('black'))
    target()
    move_missile()
    if time.time()-timer > interval:
        create_enemy()
        interval = random.randint(1,3)
        timer = time.time()
    move_enemy()
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                m = Missile()
                m.goalX,m.goalY = pg.mouse.get_pos()
                m.x = WIDTH/2
                m.y = HEIGHT-50
                x = m.goalX-m.x
                y = m.goalY-m.y
                m.angle = math.atan2(y,x)
                m.radius = 5
                m.moving = True
                missiles.append(m)
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

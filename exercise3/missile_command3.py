import pygame as pg, sys, math, random, time

WIDTH,HEIGHT = 800,600
pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('ミサイルコマンド')
clock = pg.time.Clock()
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
        if not ((m.goalX-1<=int(m.x)<=m.goalX+1) and \
                (m.goalY-1<=int(m.y)<=m.goalY+1)):
            m.x += math.cos(m.angle)*2
            m.y += math.sin(m.angle)*2
            if collide(m):
                missiles.remove(m)
        else:
            m.radius += 0.5
            if collide(m):
                missiles.remove(m)
                continue
            if m.radius > 60:
                missiles.remove(m)

def create_enemy():
    e = Missile()
    e.goalX = random.randint(50,WIDTH-50)
    e.goalY = HEIGHT
    e.startX = random.randint(0,WIDTH)
    e.startY = 0
    e.x,e.y = e.startX,e.startY
    x = e.goalX-e.x
    y = e.goalY-e.y
    e.angle = math.atan2(y,x)
    e.radius = 5
    enemies.append(e)

base = 10
over = False
def move_enemy():
    global base, over
    for e in enemies:
        pg.draw.line(screen, (255,0,0), (e.startX,e.startY), (e.x,e.y), 2)
        pg.draw.circle(screen, (255,255,255), (e.x,e.y), e.radius)
        if not ((e.goalX-1<=int(e.x)<=e.goalX+1) and \
                (e.goalY-1<=int(e.y)<=e.goalY+1)):
            e.x += math.cos(e.angle)
            e.y += math.sin(e.angle)
        else:
            base -= 1
            enemies.remove(e)
            if base <= 0:
                over = True

def collide(missile):
    for e in enemies:
         if ((e.x-missile.x)**2 + (e.y-missile.y)**2)**0.5 < e.radius+missile.radius:
             enemies.remove(e)
             return True
    return False

def draw_base():
    pg.draw.polygon(screen, (128,128,0),
                    [[WIDTH/2-50,HEIGHT-50],
                     [WIDTH/2+50,HEIGHT-50],
                     [WIDTH/2+100,HEIGHT],
                     [WIDTH/2-100,HEIGHT]])
    for i in range(base):
        x = i%5*20+(WIDTH/2-40)
        y = i//5*20+(HEIGHT-35)
        pg.draw.circle(screen, (255,0,0), (x,y), 5)        

interval = 3
timer = time.time()
while True:
    screen.fill(pg.Color('black'))
    target()
    draw_base()
    if not over:
        move_missile()
        if time.time()-timer > interval:
            create_enemy()
            interval = random.randint(1,3)
            timer = time.time()
        move_enemy()
    else:
        font = pg.font.SysFont('helvetica', 30)
        txt = font.render('GAME OVER',True,(255,0,255))
        screen.blit(txt,((WIDTH-txt.get_width())/2,(HEIGHT-txt.get_height())/2))
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            m = Missile()
            m.goalX,m.goalY = pg.mouse.get_pos()
            m.x = WIDTH/2
            m.y = HEIGHT-50
            x = m.goalX-m.x
            y = m.goalY-m.y
            m.angle = math.atan2(y,x)
            m.radius = 5
            missiles.append(m)
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    clock.tick(60)
import pygame as pg, sys, random, time

class Circle:
    def collide(self,obj):
        dist = ((self.x-obj.x)**2 + (self.y-obj.y)**2)**0.5
        return dist < self.radius+obj.radius

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('通路を抜けろ')
player = Circle()
player.x = 20
player.y = 20
player.dx = 0
player.dy = 0
player.radius = 15
walls = []
for i in range(25):
    e = Circle()
    e.radius = 26
    e.x = i%5*92+66
    e.y = i//5*92+66
    e.id = i
    walls.append(e)
goal = random.randint(0,24)
clear = False
over = False
stime = time.time()

while True:
    screen.fill(pg.Color('white'))
    key = pg.key.get_pressed()
    if key[pg.K_UP]:
        player.dy -= 0.1
    if key[pg.K_DOWN]:
        player.dy += 0.1
    if key[pg.K_RIGHT]:
        player.dx += 0.1
    if key[pg.K_LEFT]:
        player.dx -= 0.1
    if not clear and not over:
        player.dx *= 0.98
        player.dy *= 0.98
        player.x += player.dx
        player.y += player.dy

    pg.draw.circle(screen,pg.Color('black'),(player.x,player.y),player.radius)

    if player.x < player.radius or player.x > 500-player.radius or player.y < player.radius or player.y > 500-player.radius:
        over = True

    for w in walls:
        if w.id == goal:
            pg.draw.circle(screen,pg.Color('blue'),(w.x,w.y),w.radius)
        else:
            pg.draw.circle(screen,pg.Color('red'),(w.x,w.y),w.radius)
        if w.collide(player):
            if w.id == goal and not clear:
                clear = True
                etime = time.time()-stime
            elif not clear:
                over = True

    if over:
        font = pg.font.SysFont('helvetica', 30)
        txt = font.render(f'GAME OVER',True,(0,0,0))
        screen.blit(txt,((500-txt.get_width())/2,(500-txt.get_height())/2))
    if clear:
        font = pg.font.SysFont('helvetica', 30)
        txt = font.render(f'CLEAR {etime:.0f}sec',True,(0,0,0))
        screen.blit(txt,((500-txt.get_width())/2,(500-txt.get_height())/2))

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
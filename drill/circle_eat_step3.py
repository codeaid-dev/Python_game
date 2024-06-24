import pygame as pg, sys, random

class Circle:
    def collide(self,obj):
        dist = ((self.x-obj.x)**2 + (self.y-obj.y)**2)**0.5
        return dist < self.size/2+obj.size/2
        

#step2
enemies = []
def create_enemy():
    c = f'#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}'
    s = random.uniform(player.size*0.5,player.size*2)
    e = Circle()
    e.x = -s/2
    e.y = random.uniform(s/2,400-s/2)
    e.size = s
    e.color = c
    e.speed = random.randint(-3,3)
    if e.speed == 0:
        e.speed = 1
    if e.speed < 0:
        e.x = 600
    pg.draw.circle(screen,pg.Color(e.color),(e.x,e.y),e.size/2)
    enemies.append(e)

pg.init()
screen = pg.display.set_mode((600,400))
pg.display.set_caption('円を食べる（ステップ3）')
player = Circle()
player.size = 20
frame = 1
# step3
start = False
over = False

while True:
    screen.fill(pg.Color('black'))
    player.x,player.y = pg.mouse.get_pos()
    player.rect = pg.draw.circle(screen,pg.Color('white'),(player.x,player.y),player.size/2)
    # step2/step3 -->
    if start and not over: # step3
        if frame%50==0:
            create_enemy()
        for id,e in enumerate(enemies):
            e.x = e.x+e.speed
            pg.draw.circle(screen,pg.Color(e.color),(e.x,e.y),e.size/2)
            if player.collide(e):
                if player.size < e.size:
                    over = True
                else:
                    player.size += e.size*0.1
                    del enemies[id]
        frame += 1
    elif not over: # step3
        font = pg.font.SysFont('helvetica', 30)
        txt = font.render(f'Click: GAME START',True,(255,255,255))
        screen.blit(txt,((600-txt.get_width())/2,(400-txt.get_height())/2))
    else:
        font = pg.font.SysFont('helvetica', 30)
        txt = font.render(f'GAME OVER',True,(255,255,255))
        screen.blit(txt,((600-txt.get_width())/2,(400-txt.get_height())/2))
    # <-- step2/step3

    pg.display.update()
    pg.time.Clock().tick(50)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1: # step3
            start = True
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
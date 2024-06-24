import pygame as pg, sys, random

class Circle:
    pass

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
pg.display.set_caption('円を食べる（ステップ2）')
player = Circle()
player.size = 20
frame = 1

while True:
    screen.fill(pg.Color('black'))
    player.x,player.y = pg.mouse.get_pos()
    player.rect = pg.draw.circle(screen,pg.Color('white'),(player.x,player.y),player.size/2)
    # step2 -->
    if frame%50==0:
        create_enemy()
    for e in enemies:
        e.x = e.x+e.speed
        pg.draw.circle(screen,pg.Color(e.color),(e.x,e.y),e.size/2)
    frame += 1
    # <-- step2

    pg.display.update()
    pg.time.Clock().tick(50)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
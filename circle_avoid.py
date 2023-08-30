import pygame as pg, sys, random, time

class Circle:
    pass

enemies = []

pg.init()
screen = pg.display.set_mode((400,600))
pg.display.set_caption('落ちてくる円を避ける')
width,height = screen.get_size()
font = pg.font.SysFont('meiryo', 30)
for i in range(20):
    enemy = Circle()
    enemy.radius = random.randint(2,25)
    enemy.x = random.randint(enemy.radius,width-enemy.radius)
    enemy.y = random.randint(enemy.radius,height-enemy.radius)
    enemy.dy = random.randint(1,6)
    enemies.append(enemy)
start = False
over = False

while True:
    screen.fill(pg.Color('white'))
    px,py = pg.mouse.get_pos()
    pg.draw.circle(screen, pg.Color('black'), (px,py), 15)
    for enemy in enemies:
        if start and not over:
            enemy.y += enemy.dy
            if enemy.y > height-enemy.radius:
                enemy.radius = random.randint(2,25)
                enemy.x = random.randint(enemy.radius,width-enemy.radius)
                enemy.y = -enemy.radius
            if ((enemy.x-px)**2+(enemy.y-py)**2) ** 0.5 < enemy.radius+15 or 15>px or px>width-15 or 15>py or py>height-15:
                start = False
                over = True
                etime = time.time()-stime
        enemy.rect = pg.draw.circle(screen,pg.Color('red'),(enemy.x,enemy.y),enemy.radius)
    if not start and not over:
        txt = font.render('Mouse Press : Start',True,(0,0,0))
        screen.blit(txt,((width-txt.get_width())/2,(height-txt.get_height())/2))
    elif not start and over:
        txt = font.render(f'GAME OVER {etime:.0f}sec',True,(0,0,0))
        screen.blit(txt,((width-txt.get_width())/2,(height-txt.get_height())/2))

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and not start:
            start = True
            stime = time.time()

        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
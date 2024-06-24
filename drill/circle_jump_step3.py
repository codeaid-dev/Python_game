import pygame as pg, sys, random

class Circle:
    def collide(self,obj):
        dist = ((self.x-obj.x)**2 + (self.y-obj.y)**2)**0.5
        return dist < self.radius+obj.radius

pg.init()
screen = pg.display.set_mode((700,300))
pg.display.set_caption('ジャンプして避けろ')
player = Circle()
player.x = 235
player.y = 235
player.dx = 0
player.dy = 0
player.radius = 15
enemies = []
for i in range(5):
    enemy = Circle()
    enemy.radius = random.randint(10,75)
    enemy.x = random.randint(700+enemy.radius,1400-enemy.radius)
    enemy.y = 300-enemy.radius
    enemy.hit = False
    enemies.append(enemy)
hits = 0

while True:
    screen.fill(pg.Color('white'))
    if player.y > 285:
        player.dy = 0
        player.y = 285
    else:
        player.dy += 0.3
    key = pg.key.get_pressed()
    if key[pg.K_UP] and player.y >=285:
        player.dy = -12
    if key[pg.K_DOWN]:
        player.dy += 2
    if key[pg.K_RIGHT]:
        player.dx += 0.3
    if key[pg.K_LEFT]:
        player.dx -= 0.3
    player.dx *= 0.98
    player.x += player.dx
    player.y += player.dy
    pg.draw.circle(screen,pg.Color('black'),(player.x,player.y),player.radius)
    for enemy in enemies:
        if hits < 5:
            enemy.x -= 3
            if enemy.x < -enemy.radius:
                enemy.x = random.randint(700+enemy.radius,1400-enemy.radius)
        if enemy.collide(player) and not enemy.hit:
            enemy.color = 'red'
            enemy.hit = True
            hits += 1
        elif not enemy.hit:
            enemy.color = 'blue'
        pg.draw.circle(screen,pg.Color(enemy.color),(enemy.x,enemy.y),enemy.radius)
    if hits >= 5:
        font = pg.font.SysFont('helvetica', 30)
        txt = font.render(f'GAME OVER',True,(0,0,0))
        screen.blit(txt,((700-txt.get_width())/2,(300-txt.get_height())/2))

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
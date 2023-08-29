import pygame as pg, sys, random, time

def apple_setup():
    global aw,ah,ax,ay,aspeed
    aw,ah = apple.get_size()
    ax = random.randint(0,width-aw)
    ay = -ah
    aspeed = random.randint(10,20)

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('フルーツキャッチャー')
width = screen.get_width()
height = screen.get_height()
apple = pg.image.load('images/apple.png')
apple_setup()
bowl = pg.image.load('images/bowl.png')
bw,bh = bowl.get_size()
bx = (width-bw)/2
by = height-bh
catch_oto = pg.mixer.Sound('sounds/catch.mp3')
score = 0
stime = time.time()
timeup = False

while True:
    screen.fill(pg.Color('white'))
    key = pg.key.get_pressed()
    if key[pg.K_RIGHT]:
        bx += 5
    if key[pg.K_LEFT]:
        bx -= 5
    if bx < 0:
        bx += 5
    if bx > width-bw:
        bx -= 5
    brect = screen.blit(bowl,(bx,by))

    ay += aspeed
    if ay > height:
        apple_setup()
    arect = screen.blit(apple,(ax,ay))

    #落ちそうなりんごの横に当たってもキャッチしたこととなるのを修正するには
    #りんごの高さも条件に加える
    if brect.colliderect(arect) and not timeup and ay < height-ah*2/3:
    #if brect.colliderect(arect) and not timeup:
        catch_oto.play()
        score += 1
        apple_setup()

    etime = time.time() - stime
    if etime > 20:
        timeup = True
        font = pg.font.SysFont('meiryo', 30)
        text = font.render(f'TIME UP (score:{score})', True, (0,0,0))
        screen.blit(text,((width-text.get_width())/2,(height-text.get_height())/2))

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
import pygame as pg, sys, random

pg.init()
width,height = 500,800
screen = pg.display.set_mode((width,height))
pg.display.set_caption('シューティング')
jiki = pg.image.load('images/jiki.png')
w,h = jiki.get_size()
x,y = (width-w)/2,height-h
speed = 5
jiki_oto = pg.mixer.Sound('sounds/shoot.mp3')
jiki_tama = []
# step2 -->
teki = pg.image.load('images/teki.png')
teki_w,teki_h = teki.get_size()
tekis = [pg.Rect(random.randint(0,width-teki_w),random.randint(-height,-teki_h),teki_w,teki_h) for i in range(20)]
over = False
ex_oto = pg.mixer.Sound('sounds/explosion.mp3')
explosion = pg.image.load('images/bakuhatsu.png')
ex_w,ex_h = explosion.get_size()
# <-- step2

while True:
    screen.fill(pg.Color('white'))
    if over: # step2 -->
        screen.blit(explosion,(x+(w/2-ex_w/2),y+(h/2-ex_h/2)))
    else: # <-- step2
        key = pg.key.get_pressed()
        if key[pg.K_RIGHT]:
            x += speed
        if key[pg.K_LEFT]:
            x -= speed
        if key[pg.K_UP]:
            y -= speed
        if key[pg.K_DOWN]:
            y += speed

        if x > width-w:
            x -= speed
        if x < 0:
            x += speed
        if y > height-h:
            y -= speed
        if y < 0:
            y += speed

        jiki_rect = screen.blit(jiki, (x,y))

    for tama in jiki_tama:
        tama.y -= 10
        pg.draw.ellipse(screen, pg.Color('orange'), tama)
        if tama.y < -10:
            jiki_tama.remove(tama)

    # step2 -->
    for tr in tekis:
        tr.y += speed
        screen.blit(teki,tr)

        if jiki_rect.colliderect(tr) and not over:
            ex_oto.play()
            over = True

        if tr.y > height:
            tr.y = random.randint(-height,-teki_h)

        for tama in jiki_tama:
            if tama.colliderect(tr):
                jiki_tama.remove(tama)
                tr.y = random.randint(-height,-teki_h)
                break
    # step2 <--

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and not over: # step2
                jiki_oto.play()
                jiki_tama.append(pg.Rect(jiki_rect.x+jiki_rect.w/2-5,jiki_rect.y,10,10))
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
import pygame as pg, sys

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

while True:
    screen.fill(pg.Color('white'))
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

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                jiki_oto.play()
                jiki_tama.append(pg.Rect(jiki_rect.x+jiki_rect.w/2-5,jiki_rect.y,10,10))
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
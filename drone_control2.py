import pygame as pg, sys, random

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('ドローンを操作する')
img = pg.image.load('images/drone_red.png')
width,height = img.get_size()
img = pg.transform.scale(img,(width/3,height/3))
width,height = img.get_size()
x,y = (500-width)/2,(500-height)/2
speed = 5
targets = [pg.Rect(random.randint(0,490),random.randint(0,490),10,10) for i in range(100)]
flags = [False for i in range(100)]
tdx = [random.randint(1,4) for i in range(100)]
tdy = [random.randint(1,4) for i in range(100)]

while True:
    screen.fill(pg.Color('white'))
    key = pg.key.get_pressed()
    if key[pg.K_UP]:
        y -= speed
    if key[pg.K_DOWN]:
        y += speed
    if key[pg.K_RIGHT]:
        x += speed
    if key[pg.K_LEFT]:
        x -= speed

    if x < -width:
        x = 500
    if x > 500:
        x = -width
    if y < -height:
        y = 500
    if y > 500:
        y = -height

    pr = screen.blit(img, (x,y))

    for id,r in enumerate(targets):
        if r.colliderect(pr):
            flags[id] = True
            continue
        if not flags[id]:
            r.x += tdx[id]
            r.y += tdy[id]
            if r.x < 0 or r.x > 490:
                tdx[id] *= -1
            if r.y < 0 or r.y > 490:
                tdy[id] *= -1
            pg.draw.rect(screen, pg.Color('red'), r)

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
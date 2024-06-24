import pygame as pg, sys, random

pg.init()
screen = pg.display.set_mode((300,350))
pg.display.set_caption('おみくじ')
omikuji = [pg.image.load(f'images/omikuji_fuda{i}.png') for i in range(1,8)]
box = pg.image.load('images/omikuji.png')
btn = pg.image.load('images/omikuji_button.png')
fortune = None

def kuji():
    result = random.randint(1,100)
    if 1 <= result <= 2:
        num = 0
    elif 3 <= result <= 12:
        num = 1
    elif 13 <= result <= 32:
        num = 2
    elif 23 <= result <= 62:
        num = 3
    elif 53 <= result <= 82:
        num = 4
    elif 73 <= result <= 92:
        num = 5
    else:
        num = 6
    return num

while True:
    screen.fill(pg.Color('white'))
    w,h = btn.get_size()
    btn_rect = screen.blit(btn,((300-w)/2,280))
    if fortune != None:
        w,h = omikuji[fortune].get_size()
        screen.blit(omikuji[fortune],((300-w)/2,(300-h)/2))
    else:
        w,h = box.get_size()
        screen.blit(box,((300-w)/2,(300-h)/2))

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and btn_rect.collidepoint(event.pos):
                fortune = kuji()
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
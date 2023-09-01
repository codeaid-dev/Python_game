import pygame as pg, sys, random

class Hand:
    pass

pg.init()
screen = pg.display.set_mode((500,350))
pg.display.set_caption('じゃんけん')
font = pg.font.SysFont('rictydiminished', 20)
gu = Hand()
gu.text = 'グー'
gu.txt = font.render(gu.text, True, (0,0,0))
img = pg.image.load('images/janken_gu.png')
w,h = img.get_size()
gu.img = pg.transform.scale(img,(w/2,h/2))
choki = Hand()
choki.text = 'チョキ'
choki.txt = font.render(choki.text, True, (0,0,0))
img = pg.image.load('images/janken_choki.png')
w,h = img.get_size()
choki.img = pg.transform.scale(img,(w/2,h/2))
pa = Hand()
pa.text = 'パー'
pa.txt = font.render(pa.text, True, (0,0,0))
img = pg.image.load('images/janken_pa.png')
w,h = img.get_size()
pa.img = pg.transform.scale(img,(w/2,h/2))
hands = [gu,choki,pa]

pontxt = font.render('ぽん', True, (0,0,0))
youwin = font.render('あなたの勝ちです', True, (0,0,0))
comwin = font.render('コンピューターの勝ちです', True, (0,0,0))
aiko = font.render('あいこ', True, (0,0,0))

com = gu
you = gu
janken = False
result = None

while True:
    screen.fill(pg.Color('white'))
    if com == gu:
        screen.blit(gu.img,((250-gu.img.get_width())/2,(250-gu.img.get_height())/2))
    if com == choki:
        screen.blit(choki.img,((250-choki.img.get_width())/2,(250-choki.img.get_height())/2))
    if com == pa:
        screen.blit(pa.img,((250-pa.img.get_width())/2,(250-pa.img.get_height())/2))
    if you == gu:
        screen.blit(gu.img,((250-gu.img.get_width())/2+250,(250-gu.img.get_height())/2))
        gu.btn = pg.draw.rect(screen,pg.Color('gray'),(100,250,100,40))
    else:
        gu.btn = pg.draw.rect(screen,pg.Color('gray'),(100,250,100,40),5)
    screen.blit(gu.txt,(gu.btn.x+(gu.btn.w-gu.txt.get_width())/2,gu.btn.y+(gu.btn.h-gu.txt.get_height())/2))
    if you == choki:
        screen.blit(choki.img,((250-choki.img.get_width())/2+250,(250-choki.img.get_height())/2))
        choki.btn = pg.draw.rect(screen,pg.Color('gray'),(200,250,100,40))
    else:
        choki.btn = pg.draw.rect(screen,pg.Color('gray'),(200,250,100,40),5)
    screen.blit(choki.txt,(choki.btn.x+(choki.btn.w-choki.txt.get_width())/2,choki.btn.y+(choki.btn.h-choki.txt.get_height())/2))
    if you == pa:
        screen.blit(pa.img,((250-pa.img.get_width())/2+250,(250-pa.img.get_height())/2))
        pa.btn = pg.draw.rect(screen,pg.Color('gray'),(300,250,100,40))
    else:
        pa.btn = pg.draw.rect(screen,pg.Color('gray'),(300,250,100,40),5)
    screen.blit(pa.txt,(pa.btn.x+(pa.btn.w-pa.txt.get_width())/2,pa.btn.y+(pa.btn.h-pa.txt.get_height())/2))

    pon = pg.draw.rect(screen,pg.Color('gray'),(200,300,100,40))
    screen.blit(pontxt,(pon.x+(pon.w-pontxt.get_width())/2,pon.y+(pon.h-pontxt.get_height())/2))

    if janken:
        if (you == gu and com == choki) or (you == choki and com == pa) or (you == pa and com == gu):
            result = youwin
            janken = False
        elif (you == gu and com == pa) or (you == choki and com == gu) or (you == pa and com == choki):
            result = comwin
            janken = False
        else:
            result = aiko
            janken = False

    if result != None:
        screen.blit(result,((500-result.get_width())/2,(250-result.get_height())/2))

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mx,my = event.pos
            if gu.btn.collidepoint(mx,my):
                you = gu
            if choki.btn.collidepoint(mx,my):
                you = choki
            if pa.btn.collidepoint(mx,my):
                you = pa
            if pon.collidepoint(mx,my):
                com = random.choice(hands)
                janken = True
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
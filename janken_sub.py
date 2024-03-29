import pygame as pg, sys, random

hands = ['グー','チョキ','パー']
class Hand:
    def __init__(self,hand=None,img=False):
        self.text = hand
        self.select = False
        if img:
            gu = pg.image.load('images/janken_gu.png')
            w,h = gu.get_size()
            self.gu = pg.transform.scale(gu,(w/2,h/2))
            choki = pg.image.load('images/janken_choki.png')
            w,h = choki.get_size()
            self.choki = pg.transform.scale(choki,(w/2,h/2))
            pa = pg.image.load('images/janken_pa.png')
            w,h = pa.get_size()
            self.pa = pg.transform.scale(pa,(w/2,h/2))

pg.init()
screen = pg.display.set_mode((500,350))
pg.display.set_caption('じゃんけん')
select_gu = Hand(hands[0])
select_gu.select = True
select_choki = Hand(hands[1])
select_pa = Hand(hands[2])
com = Hand(hands[0],True)
you = Hand(hands[0],True)
font = pg.font.SysFont('rictydiminished', 20)
text_gu = font.render(hands[0], True, (0,0,0))
text_choki = font.render(hands[1], True, (0,0,0))
text_pa = font.render(hands[2], True, (0,0,0))
text_pon = font.render('ぽん', True, (0,0,0))

while True:
    screen.fill(pg.Color('white'))
    if com.text == hands[0]:
        screen.blit(com.gu,((250-com.gu.get_width())/2,(250-com.gu.get_height())/2))
    if com.text == hands[1]:
        screen.blit(com.choki,((250-com.choki.get_width())/2,(250-com.choki.get_height())/2))
    if com.text == hands[2]:
        screen.blit(com.pa,((250-com.pa.get_width())/2,(250-com.pa.get_height())/2))
    if you.text == hands[0]:
        screen.blit(you.gu,((250-you.gu.get_width())/2+250,(250-you.gu.get_height())/2))
    if you.text == hands[1]:
        screen.blit(you.choki,((250-you.choki.get_width())/2+250,(250-you.choki.get_height())/2))
    if you.text == hands[2]:
        screen.blit(you.pa,((250-you.pa.get_width())/2+250,(250-you.pa.get_height())/2))
    if select_gu.select:
        select_gu.rect = pg.draw.rect(screen,pg.Color('gray'),(100,250,100,40))
    else:
        select_gu.rect = pg.draw.rect(screen,pg.Color('gray'),(100,250,100,40),5)
    screen.blit(text_gu,
                (select_gu.rect.x+(select_gu.rect.w-text_gu.get_width())/2,
                 select_gu.rect.y+(select_gu.rect.h-text_gu.get_height())/2))
    if select_choki.select:
        select_choki.rect = pg.draw.rect(screen,pg.Color('gray'),(200,250,100,40))
    else:
        select_choki.rect = pg.draw.rect(screen,pg.Color('gray'),(200,250,100,40),5)
    screen.blit(text_choki,
                (select_choki.rect.x+(select_choki.rect.w-text_choki.get_width())/2,
                 select_choki.rect.y+(select_choki.rect.h-text_choki.get_height())/2))
    if select_pa.select:
        select_pa.rect = pg.draw.rect(screen,pg.Color('gray'),(300,250,100,40))
    else:
        select_pa.rect = pg.draw.rect(screen,pg.Color('gray'),(300,250,100,40),5)
    screen.blit(text_pa,
                (select_pa.rect.x+(select_pa.rect.w-text_pa.get_width())/2,
                 select_pa.rect.y+(select_pa.rect.h-text_pa.get_height())/2))

    pon = pg.draw.rect(screen,pg.Color('gray'),(200,300,100,40))
    screen.blit(text_pon,(pon.x+(pon.w-text_pon.get_width())/2,pon.y+(pon.h-text_pon.get_height())/2))

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mx,my = event.pos
            if select_gu.rect.collidepoint(mx,my):
                select_gu.select = True
                select_choki.select = False
                select_pa.select = False
                you.text = hands[0]
            if select_choki.rect.collidepoint(mx,my):
                select_choki.select = True
                select_gu.select = False
                select_pa.select = False
                you.text = hands[1]
            if select_pa.rect.collidepoint(mx,my):
                select_pa.select = True
                select_choki.select = False
                select_gu.select = False
                you.text = hands[2]
            if pon.collidepoint(mx,my):
                com.text = random.choice(hands)
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
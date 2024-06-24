import pygame as pg, sys

class Circle:
    pass

def judge():
#    global R,Y
    for i in range(len(ens)):
        if 0<=i%7<=3:
            if ens[i].color==R and ens[i+1].color==R and ens[i+2].color==R and ens[i+3].color==R:
                return 1
            if ens[i].color==Y and ens[i+1].color==Y and ens[i+2].color==Y and ens[i+3].color==Y:
                return 2
        if 0<=i//7<=2:
            if ens[i].color==R and ens[i+7].color==R and ens[i+14].color==R and ens[i+21].color==R:
                return 1
            if ens[i].color==Y and ens[i+7].color==Y and ens[i+14].color==Y and ens[i+21].color==Y:
                return 2
        if 3<=i<=6 or 10<=i<=13 or 17<=i<=20:
            if ens[i].color==R and ens[i+6].color==R and ens[i+12].color==R and ens[i+18].color==R:
                return 1
            if ens[i].color==Y and ens[i+6].color==Y and ens[i+12].color==Y and ens[i+18].color==Y:
                return 2
        if 0<=i<=3 or 7<=i<=10 or 14<=i<=17:
            if ens[i].color==R and ens[i+8].color==R and ens[i+16].color==R and ens[i+24].color==R:
                return 1
            if ens[i].color==Y and ens[i+8].color==Y and ens[i+16].color==Y and ens[i+24].color==Y:
                return 2
    return 0

pg.init()
screen = pg.display.set_mode((700,600))
pg.display.set_caption('4目並べ')
ens = []
for i in range(42):
    en = Circle()
    en.radius = 50
    en.x = i%7*en.radius*2+en.radius
    en.y = i//7*en.radius*2+en.radius
    en.color = 'white'
    ens.append(en)
R,Y = 'red','yellow'
over = 0 # 1:赤の勝ち,2:黄の勝ち
turn = False # True:赤,False:黄
font = pg.font.SysFont('rictydiminished', 70)

while True:
    screen.fill(pg.Color('gray'))
    for en in ens:
        pg.draw.circle(screen,pg.Color(en.color),(en.x,en.y),en.radius)

    if over==1:
        txt = font.render('赤の勝ち',True,(0,0,0))
        screen.blit(txt,((700-txt.get_width())/2,(600-txt.get_height())/2))
    if over==2:
        txt = font.render('黄の勝ち',True,(0,0,0))
        screen.blit(txt,((700-txt.get_width())/2,(600-txt.get_height())/2))

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mx,my = event.pos
            if over==0:
                for i,en in enumerate(ens):
                    if ((en.x-mx)**2 + (en.y-my)**2)**0.5 < en.radius:
                        if (i>=35 and en.color=='white') or (i<35 and ens[i+7].color!='white' and en.color=='white'):
                            if turn:
                                turn = False
                                en.color = R
                            else:
                                turn = True
                                en.color = Y
            over = judge()

        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
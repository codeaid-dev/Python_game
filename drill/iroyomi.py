import pygame as pg, sys, random

class Circle:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color

pg.init()
screen = pg.display.set_mode((600,600))
pg.display.set_caption('いろよみ')
iro = ['red','green','blue','yellow']
moji = ['赤','緑','青','黄']
iro_yomi = ['色','読み']
odai = [random.randint(0,3) for i in range(2)]
odai.append(random.randint(0,1))
ens = []
ens.append(Circle(300,120,'red'))
ens.append(Circle(480,300,'green'))
ens.append(Circle(300,480,'blue'))
ens.append(Circle(120,300,'yellow'))
font = pg.font.SysFont('rictydiminished', 70)
timer = 210
finish = False
score = 0

while True:
    screen.fill(pg.Color('gray'))
    for en in ens:
        pg.draw.circle(screen,pg.Color(en.color),(en.x,en.y),100)
    txt = font.render(moji[odai[0]],True,pg.Color(iro[odai[1]]))
    screen.blit(txt,((600-txt.get_width())/2,(600-txt.get_height())/2-40))
    txt = font.render(iro_yomi[odai[2]],True,(0,0,0))
    screen.blit(txt,((600-txt.get_width())/2,(600-txt.get_height())/2+40))

    if not finish:
        timer -= 1
        if int(timer/10) == 0:
            finish = True
    else:
        txt = font.render('FINISH!',True,(0,0,0))
        screen.blit(txt,((600-txt.get_width())/2,30))
    txt = font.render(str(int(timer/10)),True,(0,0,0))
    screen.blit(txt,(80,30))
    txt = font.render(str(score),True,(0,0,0))
    screen.blit(txt,(480,30))

    pg.display.update()
    pg.time.Clock().tick(10)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mx,my = event.pos
            for en in ens:
                if ((en.x-mx)**2 + (en.y-my)**2)**0.5 < 100:
                    if not finish:
                        if odai[2]==0 and iro[odai[1]]==en.color:
                            score += 1
                            odai = [random.randint(0,3) for i in range(2)]
                            odai.append(random.randint(0,1))
                        elif odai[2]==1 and iro[odai[0]]==en.color:
                            score += 1
                            odai = [random.randint(0,3) for i in range(2)]
                            odai.append(random.randint(0,1))
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
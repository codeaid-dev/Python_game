import pygame as pg, sys, random, time

class Tile():
    pass

pg.init()
screen = pg.display.set_mode((850,400))
pg.display.set_caption('同じ模様')
font = pg.font.SysFont('helvetica', 50)
status = 0 # 1:start,2:over,3:clear
lefts = []
rights = []
for i in range(25):
    left = Tile()
    left.rect = pg.Rect(i%5*80,i//5*80,80,80)
    left.color = random.choice(['red','white'])
    lefts.append(left)

    right = Tile()
    right.rect = pg.Rect(450+i%5*80,i//5*80,80,80)
    right.color = random.choice(['red','white'])
    rights.append(right)

while True:
    screen.fill(pg.Color('white'))
    for i in range(25):
        pg.draw.rect(screen,pg.Color(lefts[i].color),lefts[i].rect)
        pg.draw.rect(screen,pg.Color('black'),lefts[i].rect,1)
        pg.draw.rect(screen,pg.Color(rights[i].color),rights[i].rect)
        pg.draw.rect(screen,pg.Color('black'),rights[i].rect,1)

    if status == 0:
        txt = font.render('Click: Start',True,(0,0,0))
        screen.blit(txt,((850-txt.get_width())/2,(400-txt.get_height())/2))
    elif status == 2:
        txt = font.render('GAME OVER',True,(0,0,0))
        screen.blit(txt,((850-txt.get_width())/2,(400-txt.get_height())/2))
    elif status == 3:
        txt = font.render(f'GAME CLEAR: {etime:.0f}sec',True,(0,0,0))
        screen.blit(txt,((850-txt.get_width())/2,(400-txt.get_height())/2))

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if status == 1:
                mx,my = event.pos
                count = 0
                for i in range(25):
                    if rights[i].rect.x < mx < rights[i].rect.x+80 and rights[i].rect.y < my < rights[i].rect.y+80:
                        if rights[i].color != lefts[i].color:
                            if rights[i].color == 'red':
                                rights[i].color = 'white'
                            else:
                                rights[i].color = 'red'
                        else:
                            status = 2
                    if rights[i].color == lefts[i].color:
                        count += 1
                if count == 25:
                    status = 3
                    etime = time.time()-stime
            elif status == 0:
                status = 1
                stime = time.time()
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
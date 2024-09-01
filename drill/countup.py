import pygame as pg, sys, random, time

class Tile:
    pass

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('カウントアップ')
nums = [i for i in range(1,26)]
random.shuffle(nums)
tiles = []
for i in range(25):
    tile = Tile()
    tile.rect = pg.Rect(i%5*100,i//5*100,100,100)
    tile.num = nums[i]
    tile.color = 'red'
    tile.show = True
    tiles.append(tile)
status = 0 # 0:play,1:over,2:clear
stime = time.time()
font = pg.font.SysFont('helvetica', 30)
count = 1

while True:
    screen.fill(pg.Color('white'))
    for id,tile in enumerate(tiles):
        if tile.show and status == 0:
            pg.draw.rect(screen,pg.Color(tile.color),tile.rect)
            pg.draw.rect(screen,pg.Color('gray'),tile.rect,1)
            txt = font.render(f'{tile.num}',True,(0,0,0))
            screen.blit(txt,(id%5*100+((100-txt.get_width())/2),id//5*100+((100-txt.get_height())/2)))
    if status == 1:
        txt = font.render('GAME OVER',True,(255,0,0))
        screen.blit(txt,((500-txt.get_width())/2,(500-txt.get_height())/2))
    elif status == 2:
        txt = font.render(f'CLEAR time:{etime:.1f}sec',True,(0,128,0))
        screen.blit(txt,((500-txt.get_width())/2,(500-txt.get_height())/2))

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mx,my = event.pos
            for tile in tiles:
                if tile.rect.collidepoint(mx,my):
                    if tile.num == count:
                        tile.show = False
                        if count == 25:
                            status = 2
                            etime = time.time()-stime
                        else:
                            count += 1
                    else:
                        status = 1
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
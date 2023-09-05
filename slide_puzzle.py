import pygame as pg, sys, random

pg.init()
screen = pg.display.set_mode((450,450))
pg.display.set_caption('スライドパズル')
font = pg.font.SysFont('helvetica', 70)

side=150
nums = []
while len(nums) < 9:
    n = random.randint(0,8)
    if n not in nums:
        nums.append(n)

while True:
    screen.fill(pg.Color('gray50'))
    for i in range(9):
        pg.draw.rect(screen,pg.Color('black'),(i%3*side,i//3*side,side,side),1)
        if nums[i] != 0:
            txt = font.render(f'{nums[i]}',True,(255,255,255))
            screen.blit(txt,(i%3*side+((side-txt.get_width())/2),i//3*side+((side-txt.get_height())/2)))

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mx,my = event.pos
            for i in range(9):
                if i%3*side<mx<i%3*side+side and i//3*side<my<i//3*side+side:
                    if i <= 5 and nums[i+3]==0:
                        nums[i], nums[i+3] = nums[i+3], nums[i]
                    if i >= 3 and nums[i-3]==0:
                        nums[i], nums[i-3] = nums[i-3], nums[i]
                    if i%3 != 2 and nums[i+1]==0:
                        nums[i], nums[i+1] = nums[i+1], nums[i]
                    if i%3 != 0 and nums[i-1]==0:
                        nums[i], nums[i-1] = nums[i-1], nums[i]

        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
import pygame as pg, sys, random

WINDOW_SIZE = WIDTH,HEIGHT = 600,400
pg.init()
screen = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption('色記憶')

class Rect:
    def __init__(self,x,y,c):
        self.x = x
        self.y = y
        self.c = c
    def draw(self,c=None):
        if c==None:
            color = self.c
        else:
            color = c
        rect = pg.Rect(self.x,self.y,100,100)
        pg.draw.rect(screen,color,rect)

rects = []
colors = [(255,0,0),
          (0,255,0),
          (0,0,255),
          (255,255,0),
          (0,255,255),
          (255,0,255)]
qcolors = [False for i in range(6)]
for i in range(6):
    num = random.randint(0,5)
    if not colors[num] in qcolors:
        qcolors[num] = colors[num]
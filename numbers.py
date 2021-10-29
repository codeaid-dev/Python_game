import pgzrun
from pgzero.builtins import Actor, animate, keyboard
#import pgzero.screen
from random import randint

WIDTH = 400
HEIGHT = 400

dots = []
lines = []

next_dot = 0

for dot in range(10):
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH-20), randint(20, HEIGHT-20)
    dots.append(actor)

def draw():
    screen.fill("back")
    number = 1
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1]+12))
        dot.draw()
        number += 1
    for line in lines:
        screen.draw.line(line[0], line[1], (100,0,0))

pgzrun.go()

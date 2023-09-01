import pygame as pg

for f in pg.font.get_fonts():
    if f.startswith('r'):
        print(f,end=' ')
print('')
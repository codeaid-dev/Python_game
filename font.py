import pygame as pg

for f in pg.font.get_fonts():
#    print(f,end=' ')
    if f.startswith('m'):
        print(f,end=' ')
print('')
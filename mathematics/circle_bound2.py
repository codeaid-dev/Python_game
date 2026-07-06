import pygame as pg, math, random

WIDTH, HEIGHT = 500, 500
FPS = 60
class Circle(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((30, 30), pg.SRCALPHA)
        pg.draw.circle(self.image,(0,0,0),(15,15),15)
        self.rect = self.image.get_rect(center=(WIDTH/2, HEIGHT/2))
        self.x, self.y = WIDTH/2, HEIGHT/2
        self.speed = 5
        self.dir = random.randint(0,360)
        self.dx = self.speed*math.cos(math.radians(self.dir))
        self.dy = self.speed*math.sin(math.radians(self.dir))

    def update(self):
        mx, my = pg.mouse.get_pos()
        b1,b2,b3 = pg.mouse.get_pressed()
        if b1:
            self.x = mx
            self.y = my
            self.dir = random.randint(0,360)
            self.dx = self.speed*math.cos(math.radians(self.dir))
            self.dy = self.speed*math.sin(math.radians(self.dir))
        self.x += self.dx
        self.y += self.dy
        if self.x < 15 or self.x > WIDTH-15:
            self.dx *= -1
        if self.y < 15 or self.y > HEIGHT-15:
            self.dy *= -1
        self.rect = self.image.get_rect(center=(self.x, self.y))

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('円が画面内をウロウロする(dx,dy)')
clock = pg.time.Clock()

all_circles = pg.sprite.Group()
all_circles.add(Circle())

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    all_circles.update()
    screen.fill(pg.Color('white'))
    all_circles.draw(screen)

    pg.display.update()
    clock.tick(FPS)

pg.quit()

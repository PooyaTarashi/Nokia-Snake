import pygame as pg
import sys
import random
from pygame.math import Vector2 as v2
# from pygame.draw import rect as rct

class FOOD:
    def __init__(self):
        self.x = 0
        self.y = 10
        self.pos = v2(self.x, self.y)
    
    def draw_food(self):
        food_rect = pg.Rect(int(self.pos.x * grid_size), int(self.pos.y * grid_size), grid_size, grid_size)
        pg.draw.rect(screen, (126, 166, 114), food_rect)

# module initiatioin
pg.init()
# griding screen
grid_size = 20
x_grids_count, y_grids_count = 40, 30 
# making screen - keep it using while loop
screen = pg.display.set_mode((x_grids_count * grid_size, y_grids_count * grid_size)) 
clock = pg.time.Clock()

apple = FOOD()

while True:
    # checks for happening event
    # if quit, sys exit stops every running code
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    # add fill color to screen surface
    screen.fill((175, 215, 70))
    apple.draw_food()
    pg.display.update()
    clock.tick(60)
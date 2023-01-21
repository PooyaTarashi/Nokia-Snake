import pygame as pg
import sys
from random import randint as rnt
from pygame.math import Vector2 as v2
from pygame.draw import rect as drwrct

class SNAKE:
    def __init__(self):
        self.body = [v2(5, 10), v2(6, 10), v2(7, 10), v2(8, 10)]
        self.direction = v2(1, 0)    

    def draw_snake(self):
        for cell in self.body:
            snake_x_pos = int(cell.x * grid_size)
            snake_y_pos = int(cell.y * grid_size)
            cell_rect = pg.Rect(snake_x_pos, snake_y_pos, grid_size, grid_size)
            drwrct(screen, (0, 0, 255), cell_rect)

    def move_snake(self):
        body_copy = self.body[1:]
        body_copy.append(body_copy[len(body_copy) - 1] + self.direction)
        self.body = body_copy[:]


class FOOD:
    def __init__(self):
        self.reinitialize_random_position()
    
    def draw_food(self):
        food_rect = pg.Rect(int(self.pos.x * grid_size), int(self.pos.y * grid_size), grid_size, grid_size)
        drwrct(screen, (126, 166, 114), food_rect)

    def reinitialize_random_position(self):
        self.x = rnt(0, x_grids_count - 1)
        self.y = rnt(0, y_grids_count - 1)
        self.pos = v2(self.x, self.y)
        
# module initiatioin
pg.init()
# griding screen
grid_size = 20
x_grids_count, y_grids_count = 40, 30 
# making screen - keep it using while loop
screen = pg.display.set_mode((x_grids_count * grid_size, y_grids_count * grid_size)) 
clock = pg.time.Clock()

apple = FOOD()
snaky = SNAKE()

SCREEN_UPDATE = pg.USEREVENT
pg.time.set_timer(SCREEN_UPDATE, 90)
# عدد رو به تابعی از طول مار تبدیل خواهم کرد

while True:
    # checks for happening event
    # if quit, sys exit stops every running code
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snaky.move_snake()
        if event.type == pg.KEYDOWN and snaky.direction != (0, 1):
            if event.key == pg.K_UP or event.key == pg.K_w:
                snaky.direction = v2(0, -1)
        if event.type == pg.KEYDOWN and snaky.direction != (0, -1):
            if event.key == pg.K_DOWN or event.key == pg.K_s:
                snaky.direction = v2(0, 1)
        if event.type == pg.KEYDOWN and snaky.direction != (-1, 0):
            if event.key == pg.K_RIGHT or event.key == pg.K_d:
                snaky.direction = v2(1, 0)
        if event.type == pg.KEYDOWN and snaky.direction != (1, 0):
            if event.key == pg.K_LEFT or event.key == pg.K_a:
                snaky.direction = v2(-1, 0)
    
    # add fill color to screen surface
    screen.fill((175, 215, 70))
    apple.draw_food()
    snaky.draw_snake()
    pg.display.update()
    if apple.pos == snaky.body[0]:
        apple.reinitialize_random_position()
        if v2(snaky.body[0].x + 1, snaky.body[0].y) == snaky.body[1]:
            snaky.body.insert(0, v2(snaky.body[0].x - 1, snaky.body[0].y))
        if v2(snaky.body[0].x - 1, snaky.body[0].y) == snaky.body[1]:
            snaky.body.insert(0, v2(snaky.body[0].x + 1, snaky.body[0].y))
        if v2(snaky.body[0].x, snaky.body[0].y + 1) == snaky.body[1]:
            snaky.body.insert(0, v2(snaky.body[0].x, snaky.body[0].y - 1))
        if v2(snaky.body[0].x, snaky.body[0].y - 1) == snaky.body[1]:
            snaky.body.insert(0, v2(snaky.body[0].x, snaky.body[0].y + 1))
    # if len(snaky.body) != len(set(snaky.body)):
    #     print("You Lost!")
    clock.tick(60)
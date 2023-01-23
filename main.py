import pygame as pg
import sys
from random import randint as rnt
from pygame.math import Vector2 as v2
from pygame.draw import rect as drwrct

class SNAKE:

    def __init__(self):
        self.body = [v2(5, 10), v2(6, 10)]
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

    def position_reset(self):
        self.body = [v2(5, 10), v2(6, 10)]
        self.direction = v2(1, 0)
        for cell in self.body:
            snake_x_pos = int(cell.x * grid_size)
            snake_y_pos = int(cell.y * grid_size)
            cell_rect = pg.Rect(snake_x_pos, snake_y_pos, grid_size, grid_size)
            drwrct(screen, (0, 0, 255), cell_rect)

class FOOD:
    def __init__(self, rndm, wall_ls):
        self.reinitialize_random_position(rndm, wall_ls)
    
    def draw_food(self):
        color_tuple = (self.r_factor, self.g_factor, self.b_factor)
        food_rect = pg.Rect(int(self.pos.x * grid_size), int(self.pos.y * grid_size), grid_size, grid_size)
        drwrct(screen, color_tuple, food_rect)

    def reinitialize_random_position(self, rndm, wall_ls):
        
        if rndm % 7 == 0:
            self.r_factor = 212
            self.g_factor = 175
            self.b_factor = 55
        else:
            self.r_factor = 126
            self.g_factor = 166
            self.b_factor = 114

        while True:
            self.x = rnt(0, x_grids_count - 1)
            self.y = rnt(0, y_grids_count - 1)
            if [self.x, self.y] not in wall_ls:
                break
        
        self.pos = v2(self.x, self.y)
        

class BARRIER:
    def __init__(self):
        self.x = rnt(0, x_grids_count - 1)
        self.y = rnt(0, y_grids_count - 1)
        self.pos = v2(self.x, self.y)
    
    def draw_barrier(self, x, y):
        self.x = x
        self.y = y
        self.pos = v2(self.x, self.y)
        barrier_rect = pg.Rect(int(self.pos.x * grid_size), int(self.pos.y * grid_size), grid_size * 3, grid_size)
        drwrct(screen, (101, 67, 33), barrier_rect)

# def show_score():


# module initiatioin
pg.init()
# griding screen
grid_size = 20
x_grids_count, y_grids_count = 40, 30 
# making screen - keep it using while loop
screen = pg.display.set_mode((x_grids_count * grid_size, y_grids_count * grid_size)) 
clock = pg.time.Clock()

# add game font
font = pg.font.Font('freesansbold.ttf', 16)
menu_font = pg.font.Font('pricedow.ttf', 48)
game_over_font = pg.font.Font('freesansbold.ttf', 24)


# difficulty will be customizable by user
difficulty = 9
walls_count_x = []
walls_count_y = []
walls_pos = []

# making objects - random number for golden apples
a_random_int = rnt(0, 100)
food = FOOD(a_random_int, walls_pos)
snaky = SNAKE()
wall = BARRIER()

# updates screen
SCREEN_UPDATE = pg.USEREVENT
pg.time.set_timer(SCREEN_UPDATE, 90 - int(0.01 * int(len(snaky.body) * len(snaky.body))))

# setting primary nutritive value
arzesh_qazaei = 1

# sets random position for walls
for i in range(difficulty):
    walls_count_x.append(rnt(0, x_grids_count - 3))
    walls_count_y.append(rnt(0, y_grids_count - 1))
    for j in range(3):
        walls_pos.append([walls_count_x[i] + j, walls_count_y[i]])


def main_menu():

    walls_count_x = []
    walls_count_y = []
    walls_pos = []

    # making objects - random number for golden apples
    a_random_int = rnt(0, 100)
    food = FOOD(a_random_int, walls_pos)
    snaky = SNAKE()
    wall = BARRIER()

    snaky.position_reset()

    # sets random position for walls
    for i in range(difficulty):
        walls_count_x.append(rnt(0, x_grids_count - 3))
        walls_count_y.append(rnt(0, y_grids_count - 1))
        for j in range(3):
            walls_pos.append([walls_count_x[i] + j, walls_count_y[i]])


    screen.fill((30, 30, 30))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_KP_ENTER or event.key == pg.K_SPACE or event.key == pg.K_RETURN:
                    for  i in range(3):
                        menu_surface = menu_font.render(str(i + 1), True, (255, 255, 255))
                        menu_xpos = int((grid_size / 2) * x_grids_count)
                        menu_ypos = int((grid_size / 2 + i) * y_grids_count)
                        menu_rect = menu_surface.get_rect(center = (menu_xpos, menu_ypos))
                        screen.blit(menu_surface, menu_rect)
                        pg.display.update()
                        pg.time.delay(800)
                    
                    game_screen(arzesh_qazaei)
        

        
        
        
        menu_text = "Hit ENTER or SPACE to start the game"
        menu_surface = menu_font.render(menu_text, True, (255, 255, 255))
        menu_xpos = int((grid_size / 2) * x_grids_count)
        menu_ypos = int((grid_size / 2 - 5) * y_grids_count)
        menu_rect = menu_surface.get_rect(center = (menu_xpos, menu_ypos))
        screen.blit(menu_surface, menu_rect)


        pg.display.update()
        clock.tick(60)


def game_screen(arzesh_qazaei):
    while True:
        # checks for happening event
        # if quit, sys exit stops every running code

        # motion controls
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
    
    
        food.draw_food()
        snaky.draw_snake()

        # score table
        score_text = str(len(snaky.body) - 2)
        score_surface = font.render("Score: " + score_text, True, (56, 74, 12))
        score_xpos = int((grid_size - 1) * x_grids_count)
        score_ypos = int((grid_size - 1) * y_grids_count)
        score_rect = score_surface.get_rect(center = (score_xpos, score_ypos))
        screen.blit(score_surface, score_rect)
        # print(score_text)


        for i in range(difficulty):
            wall.draw_barrier(walls_count_x[i], walls_count_y[i])
        
        pg.display.update()
    
        # eating apples
        if food.pos == snaky.body[0] or food.pos == snaky.body[len(snaky.body) - 1]:
        
            if v2(snaky.body[0].x + 1, snaky.body[0].y) == snaky.body[1]:
                for i in range(arzesh_qazaei):
                    snaky.body.insert(0, v2(snaky.body[0].x - 1, snaky.body[0].y))
            if v2(snaky.body[0].x - 1, snaky.body[0].y) == snaky.body[1]:
                for i in range(arzesh_qazaei):
                    snaky.body.insert(0, v2(snaky.body[0].x + 1, snaky.body[0].y))
            if v2(snaky.body[0].x, snaky.body[0].y + 1) == snaky.body[1]:
                for i in range(arzesh_qazaei):
                    snaky.body.insert(0, v2(snaky.body[0].x, snaky.body[0].y - 1))
            if v2(snaky.body[0].x, snaky.body[0].y - 1) == snaky.body[1]:
                for i in range(arzesh_qazaei):
                    snaky.body.insert(0, v2(snaky.body[0].x, snaky.body[0].y + 1))
        
            a_random_int = rnt(0, 100)
            # print(a_random_int)
        
            if a_random_int % 7 == 0:
                arzesh_qazaei = 3
            else:
                arzesh_qazaei = 1

            food.reinitialize_random_position(a_random_int, walls_pos)

    
        body_checker = snaky.body[:]
        head_place = body_checker[len(body_checker) - 1]
        body_checker.remove(head_place)
    
        its_over = False

        game_over_cause = ""
        # Game Over: hitting barrier
        if snaky.body[0] in walls_pos or snaky.body[len(snaky.body) - 1] in walls_pos:
            game_over_cause += "You hit a barrier!"
            its_over = True
            break
            # sys.exit()

        # Game Over: being tied
        if head_place in body_checker:
            game_over_cause += "You were tied!"
            its_over = True
            break
            # sys.exit()

        # Game Over: hitting the wall
        if ((head_place.x * grid_size) >= (x_grids_count * grid_size)) or (head_place.y < 0) or ((head_place.y * grid_size) >= (y_grids_count * grid_size)) or  (head_place.x < 0):
            game_over_cause += "You hit the wall!"
            its_over = True
            break
            # sys.exit()
    
        
        clock.tick(60)

    if its_over:
        game_over_menu(game_over_cause)

def game_over_menu(strr):
    screen.fill((30, 30, 30))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER or event.key == pg.K_SPACE:
                    main_menu()
                if event.key == pg.K_x:
                    sys.exit()
        
        
        game_over_text = "GAME OVER!"
        game_over_surface = game_over_font.render(game_over_text, True, (255, 255, 255))
        game_over_rect = game_over_surface.get_rect(center = (int((grid_size / 2) * x_grids_count), int((grid_size / 2 - 7) * y_grids_count)))
        screen.blit(game_over_surface, game_over_rect)
        pg.display.update()

        game_over_text = strr
        game_over_surface = game_over_font.render(game_over_text, True, (255, 255, 255))
        game_over_rect = game_over_surface.get_rect(center = (int((grid_size / 2) * x_grids_count), int((grid_size / 2 - 5) * y_grids_count)))
        screen.blit(game_over_surface, game_over_rect)
        pg.display.update()

        game_over_text = "press X to exit or ENTER to get back to the main menu"
        game_over_surface = game_over_font.render(game_over_text, True, (255, 255, 255))
        game_over_rect = game_over_surface.get_rect(center = (int((grid_size / 2) * x_grids_count), int((grid_size / 2 - 3) * y_grids_count)))
        screen.blit(game_over_surface, game_over_rect)

        pg.display.update()
        clock.tick(60)


main_menu()
# game_screen(arzesh_qazaei)
import pygame
import sys

# module initiatioin
pygame.init()
# making screen - keep it using while loop
screen = pygame.display.set_mode((800, 600))
########################## comment this sandwich later
clock = pygame.time.Clock()
##########################
test_surface = pygame.Surface((30, 200))
test_surface.fill((0, 0, 255))
x_pos = 200;

while True:
    # checks for happening event
    # if quit, sys exit stops every running code
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((175, 215, 70))
    screen.blit(test_surface, (x_pos, 250))
    x_pos += 1
    pygame.display.update()
    ########################## comment this sandwich later
    clock.tick(60)
    ##########################
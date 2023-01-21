import pygame
import sys

# module initiatioin
pygame.init()
# making screen - keep it using while loop
screen = pygame.display.set_mode((800, 600)) 
clock = pygame.time.Clock()

while True:
    # checks for happening event
    # if quit, sys exit stops every running code
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # add fill color to screen surface
    screen.fill((175, 215, 70))
    pygame.display.update()
    clock.tick(60)
import pygame
import sys

# module initiatioin
pygame.init()
# making screen - keep it using while loop
screen = pygame.display.set_mode((800, 600))
while True:
    # checks for happening event
    # if quit, sys exit stops every running code
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
import pygame
import sys

# module initiatioin
pygame.init()
# making screen - keep it using while loop
screen = pygame.display.set_mode((800, 600)) 
clock = pygame.time.Clock()
test_surface = pygame.Surface((30, 200))
test_surface.fill((0, 0, 255))
# test_rect = pygame.Rect(0, 0, 100, 200)
test_rect = test_surface.get_rect(center = (400, 300))
x_pos = 200;

while True:
    # checks for happening event
    # if quit, sys exit stops every running code
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((175, 215, 70))
    # screen.blit(test_surface, (x_pos, 250))
    test_rect.left += 1
    screen.blit(test_surface, test_rect)
    # pygame.draw.ellipse(screen, (255, 255, 255), test_rect)
    x_pos += 1
    pygame.display.update()
    ########################## comment this sandwich later
    clock.tick(60)
    ##########################
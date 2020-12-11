import pygame
from Projectile import *
from Tank import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (37, 37, 38)
WIDTH = 800
HEIGHT = 600


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

screen.fill(GRAY)
field = [500, 550, 580, 500, 500, 550, 500]
tank = Tank(field, 600, 800)

proyectils = []

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                tank.left()
            if event.key == pygame.K_RIGHT:
                tank.rigth()
            if event.key == pygame.K_UP:
                tank.up()
            if event.key == pygame.K_DOWN:
                tank.down()
            if event.key == pygame.K_SPACE:
                proyectils.append(tank.shot())
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                tank.stop()
            if event.key == pygame.K_RIGHT:
                tank.stop()
            if event.key == pygame.K_DOWN:
                tank.stop_gun()
            if event.key == pygame.K_UP:
                tank.stop_gun()
        
    screen.fill(GRAY)
    #draw zone
    deltaX = WIDTH//(len(field)-1)
    for i in range(1, len(field)):
        pygame.draw.line(screen, WHITE, (deltaX*(i-1), field[i-1]), (deltaX*i, field[i]))
    tank.draw(screen)
    tank.update()
    for elem in proyectils:
        elem.draw(screen)
        elem.update()
    #update screen
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

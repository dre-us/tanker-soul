import pygame, sys
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (800, 600)
screen = pygame.display.set_mode(size)
#screen.fill(WHITE)
terreno = [400, 300, 100, 200, 150, 200, 230]
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(WHITE)
    deltaX = 800//(len(terreno)-1)
    for i in range(1, len(terreno)+1):
        if i != len(terreno):
            pygame.draw.line(screen, BLACK, (deltaX*(i-1), terreno[i-1]), (deltaX*i, terreno[i]))
    pygame.display.flip()
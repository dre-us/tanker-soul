import pygame, sys
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SPEED = 5
WIDTH = 800
HEIGTH = 600
WIDTH_TANK = 20
HEIGTH_TANK = 20
STOP = 0

size = (WIDTH, HEIGTH)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
#screen.fill(WHITE)
terreno = [400, 300, 100, 200, 150, 200, 230]

pos_x = WIDTH_TANK//2
pos_y = terreno[0]

speed_x = 0
speed_y = 0

while True:
    print(pos_x)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -SPEED
            if event.key == pygame.K_RIGHT:
                speed_x = SPEED
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print("no")
                speed_x = STOP
            if event.key == pygame.K_RIGHT:
                speed_x = STOP
        
    screen.fill(WHITE)
    #draw zone
    deltaX = 800//(len(terreno)-1)
    for i in range(1, len(terreno)):
        if deltaX*(i-1) <= pos_x <= deltaX*i:
            slope = (terreno[i-1] - terreno[i])/(deltaX*(i-1) - deltaX*i)
            pos_y = slope*(pos_x-deltaX*i) + terreno[i]
        pygame.draw.line(screen, BLACK, (deltaX*(i-1), terreno[i-1]), (deltaX*i, terreno[i]))
    if pos_x < WIDTH_TANK//2:
        pos_x = WIDTH_TANK//2
    if pos_x > WIDTH-WIDTH_TANK//2:
        pos_x = WIDTH-WIDTH_TANK//2
    pygame.draw.rect(screen, RED, (pos_x-WIDTH_TANK//2, pos_y-HEIGTH_TANK//2, WIDTH_TANK, HEIGTH_TANK))
    pos_x += speed_x
    
    #update scree
    pygame.display.flip()
    clock.tick(60)
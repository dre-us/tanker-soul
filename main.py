import pygame, sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SPEED = 5
WIDTH = 800
HEIGTH = 600
WIDTH_TANK = 80
HEIGTH_TANK = 80
STOP = 0
RIGTH = 1
LEFT = -1

class Tank(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("tank.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGTH))
clock = pygame.time.Clock()
all_sprite_list = pygame.sprite.Group()

screen.fill(WHITE)
#backgroud = pygame.image.load("dir.png").convert()
#backgroud.set_colorkey(255, 255, 255)
terreno = [400, 300, 100, 200, 150, 200, 230]
tanque = Tank()
pos_x = 0
pos_y = terreno[0]-HEIGTH_TANK//2
speed_x = 0
speed_y = 0
speed_angle = 0
angle = 0
direction = RIGTH
tanque.rect.x = pos_x
tanque.rect.y = pos_y
all_sprite_list.add(tanque)

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -SPEED
                direction = LEFT
            if event.key == pygame.K_RIGHT:
                speed_x = SPEED
                direction = RIGTH
            if event.key == pygame.K_UP:
                speed_angle = 1
            if event.key == pygame.K_DOWN:
                speed_angle = -1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed_x = STOP
            if event.key == pygame.K_RIGHT:
                speed_x = STOP
            if event.key == pygame.K_DOWN:
                speed_angle = STOP
            if event.key == pygame.K_UP:
                speed_angle = STOP
        
    screen.fill(WHITE)
    #draw zone
    deltaX = WIDTH//(len(terreno)-1)
    for i in range(1, len(terreno)):
        if deltaX*(i-1) <= pos_x <= deltaX*i:
            slope = (terreno[i-1] - terreno[i])/(deltaX*(i-1) - deltaX*i) #pendiente del segmento en el cual esta el tanque
            pos_y = slope*(pos_x-deltaX*i) + terreno[i] #ecuacion de la recta para hallar el punto y donde se debe posicionar el tanque
        pygame.draw.line(screen, BLACK, (deltaX*(i-1), terreno[i-1]), (deltaX*i, terreno[i]))
    if pos_x < WIDTH_TANK//2:
        pos_x = WIDTH_TANK//2
    if pos_x > WIDTH-WIDTH_TANK//2:
        pos_x = WIDTH-WIDTH_TANK//2
    if angle > 90:
        angle = 90
    if angle < 0:
        angle = 0
    tanque.rect.x = pos_x-WIDTH_TANK//2
    tanque.rect.y = pos_y-HEIGTH_TANK
    all_sprite_list.draw(screen)
    pos_x += speed_x
    angle += speed_angle
    #update screen
    #screen.blit(backgroud, (0, 0))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

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

class Tank(object):

    def __init__(self):
        self.image_rigth = pygame.image.load("tank.png").convert()
        self.image_left = pygame.image.load("tank2.png").convert()
        self.image_rigth.set_colorkey(BLACK)
        self.image_left.set_colorkey(BLACK)
        self.image = self.image_rigth
        self.x = 0
        self.y = 0
    def move(self, x, y):
        if self.x < x:
            self.image = self.image_rigth
        elif x < self.x:
            self.image = self.image_left
        self.x = x
        self.y = y
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

class Proyectil(object):

    def __init__(self, x, y, vx, vy, radius):
        self.xi = x
        self.yi = y
        self.x = self.xi
        self.y = self.yi
        self.vxi = vx
        self.vyi = -vy
        self.t = 0
        self.radius = radius

    def update(self):
        self.t += 1
        self.x = self.xi + self.vxi*self.t
        self.y = self.yi + self.vyi*self.t + 4.9*self.t*self.t

    def draw(self, surface):
        pygame.draw.circle(surface, BLACK, (self.x, self.y), self.radius)



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGTH))
clock = pygame.time.Clock()
all_sprite_list = pygame.sprite.Group()

screen.fill(WHITE)
#backgroud = pygame.image.load("dir.png").convert()
#backgroud.set_colorkey(255, 255, 255)
terreno = [500, 550, 580, 600, 600, 550, 500]
tanque = Tank()
pos_x = WIDTH_TANK//2
pos_y = terreno[0]-HEIGTH_TANK
speed_x = 0
speed_y = 0
speed_angle = 0
angle = 0
direction = RIGTH
tanque.x = pos_x
tanque.y = pos_y
#all_sprite_list.add(tanque)

proyectils = []

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
            if event.key == pygame.K_SPACE:
                if direction == RIGTH:
                    proyectils.append(Proyectil(pos_x+35, pos_y-WIDTH_TANK, 50, 10,5))
                else:
                    proyectils.append(Proyectil(pos_x-35, pos_y-WIDTH_TANK, -50, 10,5))
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
    tanque.move(pos_x-WIDTH_TANK//2, pos_y-HEIGTH_TANK)
    for elem in proyectils:
        elem.draw(screen)
        elem.update()
    tanque.draw(screen)
    #all_sprite_list.draw(screen)
    pos_x += speed_x
    angle += speed_angle

    #update screen
    #screen.blit(backgroud, (0, 0))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

import pygame
from math import sin, cos, pi
from Projectile import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Tank(object):

    def __init__(self, field, heigth, width):
        self.speed = 0
        self.angle = 0
        self.east = 1
        self.weast = -1
        self.width = 80
        self.heigth = 80
        self.health = 100
        self.momentum = 80
        self.speed_angle = 0
        self.field = field
        self.width_map = width
        self.heigth_map = heigth
        self.x = self.width//2
        self.direction = self.east
        self.delta_x = self.width_map//(len(self.field)-1)
        self.y = self.calculate_y(self.x, 1)

        self.image_rigth = pygame.image.load("tank.png").convert()
        self.image_left = pygame.image.load("tank2.png").convert()
        self.image_rigth.set_colorkey(BLACK)
        self.image_left.set_colorkey(BLACK)
        self.image = self.image_rigth

    def shot(self):
        radians = self.angle * pi / 180
        if self.direction == self.east:
            return Projectile(self.x+45, self.y-self.width, self.momentum*cos(radians), self.momentum*sin(radians), 5)
        else:
            return Projectile(self.x-45, self.y-self.width, -self.momentum*cos(radians), self.momentum*sin(radians), 5)
    
    def update(self):
        if self.speed != 0:
            pos_x = self.x + self.speed
            pos_y = self.y
            for i in range(1, len(self.field)):
                if self.delta_x*(i-1) <= pos_x <= self.delta_x*i:
                    pos_y = self.calculate_y(pos_x, i)
            self.x = pos_x
            self.y = pos_y
        if self.speed_angle != 0:
            self.angle += self.speed_angle
            if self.angle > 90:
                self.angle = 90
            elif self.angle < 0:
                self.angle = 0

    def stop(self):
        self.speed = 0
    
    def rigth(self):
        self.direction = self.east
        self.image = self.image_rigth
        self.speed = 5

    def left(self):
        self.direction = self.weast
        self.image = self.image_left
        self.speed = -5
    
    def up(self):
        self.speed_angle = 0.5

    def down(self):
        self.speed_angle = -0.5

    def stop_gun(self):
        self.speed_angle = 0

    def calculate_y(self, pos_x, i):
        slope = (self.field[i-1] - self.field[i])/(self.delta_x*(i-1) - self.delta_x*i) #pendiente del segmento en el cual esta el tanque
        pos_y = slope*(pos_x-self.delta_x*i) + self.field[i] #ecuacion de la recta para hallar el punto y donde se debe posicionar el tanque
        return pos_y

    def draw(self, surface):
        surface.blit(self.image, (self.x-self.width//2, self.y-self.heigth))

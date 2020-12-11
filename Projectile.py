import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Projectile(object):

    def __init__(self, x, y, vx, vy, radius):
        self.g = 9.8
        self.t = 0
        self.xi = x
        self.yi = y
        self.vxi = vx
        self.vyi = -vy
        self.x = self.xi
        self.y = self.yi
        self.radius = radius
        self.width = 100
        self.height = 74
        self.damage = 50

    def update(self):
        self.t += 0.15
        self.x = self.xi + self.vxi*self.t
        self.y = self.yi + self.vyi*self.t + self.g*self.t*self.t

    def draw(self, surface):
        pygame.draw.circle(surface, (252, 92, 96), (self.x, self.y), self.radius)
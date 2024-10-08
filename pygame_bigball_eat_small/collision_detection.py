from enum import Enum, unique
from math import sqrt
from random import randint

import pygame

@unique
class Color(Enum):
    RED = (250, 0 , 0)
    Green = (0, 255 ,0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255,255,255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """获得随机颜色"""

        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        return (r, g, b)

class Ball(object):
    def __init__(self,x, y, radius, sx, sy, color=Color.RED):
       self.x= x
       self.y = y
       self.radius = radius
       self.sx = sx
       self.sy = sy
       self.color = color
       self.alive = True 

    def move(self, screen):
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or \
            self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or \
            self.y + self.radius >= screen.get_width():
            self.sy = -self.sy
    
    def eat(self, other):
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 +  dy ** 2)
            if distance < self.radius + other.radius \
                and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)
    
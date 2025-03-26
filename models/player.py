from pyray import *
from raylib import *

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vel = 3.5
        self.acc = 0
        self.friccion = 0.9
        self.rect = Rectangle(492, 500, 20, 20)
    
    def draw(self):
        draw_rectangle_rec(self.rect, BLUE)
        
    def up(self):
        self.rect.y = -self.vel
        
    def down(self):
        self.recty = self.vel
        
    def left(self):
        if self.rect.x < 0:
            self.rect.x = 1024 - self.rect.width
        self.acc = -self.vel
        
    def right(self):
        if self.rect.x > 1024 - self.rect.width:
            self.rect.x = 0
        self.acc = self.vel

    def update(self):
        self.x = self.acc * self.friccion
        self.acc = self.x
        self.rect.x += self.x
        # self.rect.y = self.y
    
    def reset(self):
        self.x = 0
        self.y = 0
        self.acc = 0
        self.rect.x = 492
        self.rect.y = 500
        self.update()
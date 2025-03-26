import random
from pyray import *
from models.timer import Timer
from utils.colision import colision_rect_circle

class Enemy:
    def __init__(self):
        self.rect = Rectangle(1024, 300, 70, 20)
        self.x = self.rect.x
        self.y = self.rect.y

        self.bullets = []

        self.destiny_x = 0
        self.destiny_y = 0
        self.rango = 50
        self.vel = 5
        self.finding = True

        self.timer_walk = Timer()
        self.timer_bullet = Timer()

    def calculate_new_destiny(self):
        self.destiny_x = random.randint(0, 950)
        self.destiny_y = random.randint(0, 300)

    def draw(self):
        self.update()
        draw_rectangle_rec(self.rect, RED)

        self.shoot()
        self.update_bullet()

    def check_colision(self, player_rect):
        for bullet in self.bullets:
            v = Vector2(bullet['x'], bullet['y'])
            if colision_rect_circle(v, 8, player_rect):
                return True

    def update(self):
        if not self.finding:
            if self.timer_walk.compare_time(random.randint(1, 6)):
                self.calculate_new_destiny()
                self.finding = True
                self.timer_walk.reset()
        else:
            self.find_destiny()

    def find_destiny(self):
        walking = [False, False]

        if abs(self.rect.x - self.destiny_x) > self.rango:   
            if self.destiny_x > self.rect.x:
                self.x = self.vel
            else:
                self.x = -self.vel
            walking[0] = True
        
        if abs(self.rect.y - self.destiny_y) > self.rango:
            if self.destiny_y > self.rect.y:
                self.y = self.vel
            else:
                self.y = -self.vel

            walking[1] = True
        
        self.rect.x += self.x
        self.rect.y += self.y

        if not any(walking): self.finding = False
    
    def create_bullet(self):
        return {
            'x': self.rect.x + self.rect.width//2,
            'y': self.rect.y,
            'velocity': random.randint(3, 10)
        }
    
    def draw_bullet(self, bullet_x, bullet_y):
        draw_circle(int(bullet_x), int(bullet_y), 8, RED)

    def update_bullet(self):
        for index, bullet in enumerate(self.bullets):
            
            bullet['y'] += bullet['velocity']
            self.bullets[index] = bullet
            self.draw_bullet(bullet['x'], bullet['y'])

            if bullet['y'] > 600:
                self.bullets.remove(bullet)

    def shoot(self):
        if self.timer_bullet.compare_time(random.randint(1, 3)):
            self.bullets.append(self.create_bullet())
            self.timer_bullet.reset()
            
    def reset(self):
        self.rect.x = 1024
        self.rect.y = 300
        self.x = self.rect.x
        self.y = self.rect.y
        self.bullets.clear()
        self.calculate_new_destiny()
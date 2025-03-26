import random

from pyray import Rectangle, draw_rectangle_rec
from raylib import WHITE

from utils.colision import colision_rect


class Lluvia:
    def __init__(self):
        self.lista_lluvia = []

    def crear_lluvia(self):
        self.lista_lluvia.clear()
        for _ in range(20):
            x = random.randint(0, 1009)
            y = random.randint(-100, 0)
            r = Rectangle(x, y, 5, 20)
            self.lista_lluvia.append([r, random.randint(5, 15)])
    
    def dibujar_lluvia(self):
        for lluvia, _ in self.lista_lluvia:
            draw_rectangle_rec(lluvia, WHITE)
    
    def actualizar_lluvia(self, player_rect):
        for lluvia, vel in self.lista_lluvia:
            lluvia.y += vel
            
            if colision_rect(lluvia, player_rect):
                return True
            
            if lluvia.y > 600:
                self.subir_lluvia(lluvia, vel)
        return False
    
    def subir_lluvia(self, lluvia, vel):
        # Obtener indice actual de la lluvia
        index_lluvia = self.lista_lluvia.index([lluvia, vel])
        # Actualizar la lluvia
        lluvia.x = random.randint(0, 1009)
        lluvia.y = random.randint(-100, 0)
        # Actualizar velocidad
        vel = random.randint(5, 15)
        # Insertar nueva lluvia
        self.lista_lluvia.insert(index_lluvia, [lluvia, vel])
        # Eliminar lluvia antigua
        self.lista_lluvia.pop(index_lluvia+1)
    
    def reset(self):
        self.crear_lluvia()
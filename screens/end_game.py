
from pyray import begin_drawing, clear_background, draw_text, end_drawing
from raylib import BLACK, YELLOW, RED
from utils.score_points import show_high_score

class EndGame:
    def __init__(self):
        self.opacidad = 255
    
    def draw(self):
        begin_drawing()

        draw_text("Presiona enter para Reiniciar", 340, 240, 20, [255, 255, 255, self.opacidad])
        draw_text("Game Over", 300, 300, 80, RED)
    
        code_puntos = show_high_score()

        draw_text(f"Score: {" - ".join(code for code in code_puntos)}", 390, 400, 25, YELLOW)

        clear_background(BLACK)
        
        end_drawing()

    def update_opacity(self):
        self.opacidad -= 4
        if self.opacidad <= 0: self.opacidad = 255
    
    def show(self):
        self.draw()
        self.update_opacity()
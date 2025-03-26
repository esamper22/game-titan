
from pyray import begin_drawing, clear_background, draw_text, end_drawing, is_key_down, is_key_released
from raylib import BLACK, YELLOW, WHITE, KEY_DOWN, KEY_UP, KEY_ENTER

class BeginGame:
    def __init__(self):
        self.menu = ['Iniciar Juego', 'Opciones', 'Salir']
        self.selected = None
        self.current_option = 1
        self.showing = True

    def draw(self):
        begin_drawing()
        
        for index, menu in enumerate(self.menu, start=1):
            sep = 80
            if index == self.current_option: draw_text(menu, 400, 130+(sep*index), 40, YELLOW)
            else: draw_text(menu, 400, 130+(sep*index), 40, WHITE)
        
        draw_text("->", 320, 130+(80*self.current_option), 40, YELLOW)

        clear_background(BLACK)
        end_drawing()

    def event(self):
        if is_key_released(KEY_UP):
            self.current_option -= 1 
        if is_key_released(KEY_DOWN):
            self.current_option += 1
        
        if self.current_option < 1: self.current_option = 1
        if self.current_option > len(self.menu): self.current_option = len(self.menu)

        if is_key_down(KEY_ENTER):
            self.selected = self.menu[self.current_option-1]
    
    def show(self):
        if self.showing:
            self.event()
            self.draw()
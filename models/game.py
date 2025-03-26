from pyray import *
from raylib import *
from models.enemy import Enemy
from models.player import Player
from models.lluvia import Lluvia
from models.music import Music
from models.timer import Timer
from utils.score_points import save_high_score, create_high_score
from screens.controller_screen import screens

class Game:
    def __init__(self):
        init_window(1024, 600, 'Game Titan')
        init_audio_device()
        set_target_fps(60)
    
    def initial_config(self):
        # Creando Objetos de mi juego
        self.player = Player()
        self.lluvia = Lluvia()
        self.enemy = Enemy()
        self.timer_point = Timer()
        self.sondio = Music("assets/sounds/Undertale.mp3")

        # Creando variables acumulativas
        self.game_over = False
        self.puntuacion = 0
        
        # Pre inicializando juego
        self.lluvia.crear_lluvia()
        self.sondio.play()
        self.enemy.calculate_new_destiny()
        create_high_score()
   
    def events(self):
        if is_key_down(KEY_DOWN):
            self.player.down()
        if is_key_down(KEY_UP):
            self.player.up()
        if is_key_down(KEY_LEFT):
            self.player.left()
        if is_key_down(KEY_RIGHT):
            self.player.right()
               
    def reset(self):
        self.player.reset()
        self.lluvia.reset()
        self.timer_point.reset()
        self.sondio.reset()
        self.enemy.reset()

        self.game_over = False
        self.puntuacion = 0
              
    def draw(self):
        begin_drawing()

        self.lluvia.dibujar_lluvia()
        self.player.draw()
        if self.puntuacion > 50: self.enemy.draw()

        draw_fps(0, 0)
        draw_text(f"Puntuacion: {self.puntuacion}", 920, 10, 12, GREEN)
        clear_background(BLACK)

        end_drawing()
    
    def bucle_principal(self):
        self.initial_config()
        
        while not window_should_close():
            screens['inicio'].show()
            selected = screens['inicio'].selected

            match selected:
                case 'Iniciar Juego':
                    screens['inicio'].showing = False
                    self.playing() if not self.game_over else self.not_playing()
                case 'Opciones':
                    pass
                case 'Salir':
                    self.unload()
                    break
            
            # print(selected)
    
    def playing(self):
        # Actualizar musica
        self.sondio.update()

        # Incrementar puntuacion
        if self.timer_point.compare_time(): 
            self.puntuacion += 5
            self.timer_point.reset()
            
        # Eventos
        self.events()

        # Actualizacion
        if self.lluvia.actualizar_lluvia(self.player.rect) or \
            self.enemy.check_colision(self.player.rect):
            save_high_score(self.puntuacion)
            self.game_over = True
            
        self.player.update()
        # Fisicas
        # Dibujados
        self.draw()

    def not_playing(self):
        self.sondio.stop()
        screens['fin'].show()
        if is_key_pressed(KEY_ENTER): self.reset()
    
    def unload(self):
        self.sondio.unload()
        close_window()

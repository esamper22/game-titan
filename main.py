from models.game import  Game
from threading import Thread
from utils.build import create_exe
def main_game():
    nuevo_juego = Game()
    nuevo_juego.bucle_principal()
        

if __name__ == "__main__":
    exe = Thread(target=create_exe)
    exe.start()

    main_game()
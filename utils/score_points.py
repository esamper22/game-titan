import os

def create_high_score():
    try:
        if not os.path.exists('punto maximo.txt'):
            with open('punto maximo.txt', 'w'):
                pass
    except Exception as e:
        print(f"Error al crear el archivo de puntuación máxima: {e}")

def save_high_score(puntuacion):
    try:
        with open('punto maximo.txt', 'r') as file:
            value = file.read().strip().split('\n')
            if value[-1]:
                high_score = int(value[-1])                                    
                if int(high_score) < puntuacion:
                    with open('punto maximo.txt', 'a') as file:
                        file.write(f'{puntuacion}\n')
            else:
                with open('punto maximo.txt', 'w') as file:
                    file.write(f'{puntuacion}\n')
    except FileNotFoundError:
        print("El archivo 'punto maximo.txt' no existe. Creándolo ahora...")
        create_high_score()
        save_high_score(puntuacion)
    except ValueError:
        print("Error al procesar los datos del archivo. Verifica el contenido.")
    except Exception as e:
        print(f"Error al guardar la puntuación máxima: {e}")

def show_high_score():
    try:
        with open('punto maximo.txt', 'r') as file:
            puntos = file.read().strip().split('\n')
            puntos.reverse()
            if len(puntos) >= 3:
                code_puntos = puntos[0:3]
            elif len(puntos) == 2:
                code_puntos = puntos[0:2]
            else:
                code_puntos = puntos
        
            return code_puntos
    except FileNotFoundError:
        print("El archivo 'punto maximo.txt' no existe. Creándolo ahora...")
        create_high_score()
        return []
    except Exception as e:
        print(f"Error al mostrar la puntuación máxima: {e}")
        return []
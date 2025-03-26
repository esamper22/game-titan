# Game Titan

Game Titan es un emocionante juego de estilo pixel art en el que el objetivo principal es esquivar obstáculos y alcanzar la mayor puntuación posible. Diseñado para ofrecer una experiencia divertida y desafiante, este juego es perfecto para los amantes de los juegos retro y minimalistas.

## Características

- **Estilo Pixel Art**: Gráficos retro que evocan la nostalgia de los videojuegos clásicos.  
- **Jugabilidad Simple y Adictiva**: Solo necesitas esquivar obstáculos para sobrevivir y mejorar tu puntuación.  
- **Portabilidad**: Juega de inmediato descargando el archivo ejecutable.  

## ¿Cómo Jugar?

### Opción 1: Descargar y Jugar

No necesitas ejecutar el código fuente ni instalar dependencias. Simplemente descarga el archivo `dist.zip` desde la carpeta `dist` del repositorio, descomprímelo y haz doble clic en el archivo `.exe` para comenzar a jugar.

**Nota**: Si encuentras un error al descomprimir el archivo `dist.zip`, puede deberse a que `shutil` utiliza un método de compresión que no es compatible con algunos descompresores. En este caso, sigue estos pasos:

1. Descarga el archivo `compress.py` desde la carpeta `utils` del repositorio.
2. Coloca el archivo `compress.py` en la misma ruta donde se encuentra el archivo `dist.zip`.
3. Ejecuta el script para descomprimir correctamente el archivo:

    ```bash
    python compress.py
    ```

Esto generará los archivos descomprimidos en la misma carpeta.

### Opción 2: Ejecutar desde el Código Fuente

Si prefieres explorar el código o realizar modificaciones, sigue estos pasos:

1. **Clonar el Repositorio**:  
    Clona el repositorio desde GitHub:  

    ```bash
    git clone https://github.com/esamper22/game-titan.git
    cd game-titan
    ```

2. **Instalar Dependencias**:  
    Asegúrate de instalar las dependencias listadas en el archivo `requirements.txt`:  

    ```bash
    pip install -r requirements.txt
    ```

3. **Ejecutar el Juego**:  
    Ejecuta el archivo principal del juego con Python:  

    ```bash
    python main.py
    ```

## Créditos

Este proyecto fue desarrollado como un homenaje a los juegos clásicos de estilo pixel art. ¡Esperamos que lo disfrutes y compartas con tus amigos!

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).  

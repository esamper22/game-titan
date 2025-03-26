import os
import subprocess

from utils.compress import create_compressed_directory


def comprimir_exe():
    if os.path.exists("dist/GameTittan.exe"):
        create_compressed_directory("dist")
        
def create_exe():
    try:
        if not os.path.exists("dist") or not os.path.exists("build") or not os.path.exists("GameTittan.exe"):
            subprocess.run(
                "pyinstaller --name GameTittan --onefile --windowed --icon=tittan.ico main.py",
                check=True
            )
            comprimir_exe()
        else:
            print("Ya existe el directorio dist o build")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar PyInstaller: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
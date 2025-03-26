import os
import subprocess

def create_exe():
    try:
        if not os.path.exists("dist") or not os.path.exists("build"):
            subprocess.run(
                "pyinstaller --name GameTittan --onefile --windowed --icon=tittan.ico main.py",
                check=True
            )
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar PyInstaller: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
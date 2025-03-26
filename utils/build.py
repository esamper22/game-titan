import os
import subprocess

def create_exe():
    if not os.path.exists("dist") or not os.path.exists("build"):
        subprocess.run("pyinstaller --name GameTittan --onefile --windowed --icon=tittan.ico main.py")
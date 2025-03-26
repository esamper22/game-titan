import os
import shutil

def create_compressed_directory(directory_path):
    try:
        if not os.path.isdir(directory_path):
            print(f"Error: '{directory_path}' no es un directorio.")
            return
        
        output_filename = directory_path.rstrip(os.sep) + '.zip'
        shutil.make_archive(directory_path, 'zip', directory_path)
        if os.path.exists(output_filename): shutil.rmtree(directory_path)
        
        print(f"Directorio comprimido exitosamente en: {output_filename}")
    except FileNotFoundError:
        print(f"Error: El directorio '{directory_path}' no existe.")
    except PermissionError:
        print(f"Error: No tienes permisos para acceder al directorio '{directory_path}'.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

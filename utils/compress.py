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

def descrompress_directory(zip_file_path):
    try:
        if not os.path.isfile(zip_file_path):
            print(f"Error: '{zip_file_path}' no es un archivo.")
            return
        
        output_directory = zip_file_path.replace('.zip', '')
        shutil.unpack_archive(zip_file_path, output_directory)
        
        print(f"Directorio descomprimido exitosamente en: {output_directory}")
    except FileNotFoundError:
        print(f"Error: El archivo '{zip_file_path}' no existe.")
    except PermissionError:
        print(f"Error: No tienes permisos para acceder al archivo '{zip_file_path}'.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

if __name__ == '__main__':
    if os.path.exists('dist.zip'): descrompress_directory('dist.zip')
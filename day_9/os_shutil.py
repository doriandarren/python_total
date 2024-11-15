import os
import shutil
import send2trash


##print(os.getcwd())

archivo = open('curso.txt', 'w')
archivo.write("Texto de prueba")
archivo.close()

## print(os.listdir())

## Mueve el archivo
## shutil.move('curso.txt', '/Users/dorian/Documents')


## mover al archivo 
send2trash.send2trash('curso.txt')


#
## Buscar elementos en un arbol de carpetas
#
ruta = '/Users/dorian/Documents'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta {ruta}')
    print(f"Las subcarpetas son:")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print(f"\t{sub}")
    for arch in archivo:
        if arch.startswith('2015'): ## Filtrar por 2015
            print(f"\t{arch}")
    print("\n")
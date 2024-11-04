import os
from pathlib import Path

from day_6.EntradaSalida import mi_archivo

ruta = os.getcwd() ## getcwd = get Current Working Directory
print(ruta)



os.chdir('/Users/dorian/Documents') ## Change directory
archivo = open("ExamplePython.txt")
print(archivo.read())





ruta = '/Users/dorian/PythonProjects/cursos/python_total/day_6/prueba2.txt'
# elem = os.path.basename(ruta) ## Retorna la path del archivo
elem = os.path.dirname(ruta) ## Retorna la path de la carpeta donde esta el archivo
print(elem)


os.makedirs('/Users/dorian/Documents/ExampleDirectorioPython') ## Crear directorio

os.rmdir('/Users/dorian/Documents/ExampleDirectorioPython') ## elimina el directorio



otro_archivo = open('/Users/dorian/Documents/ExamplePython.txt')
print(otro_archivo.read())


## Para el path
## Sirve para diferentes entornos de Sistemas Operativos

carpeta = Path('/Users/dorian/Documents/')  / 'ExamplePython.txt'

##archivo = carpeta / 'ExamplePython.txt'

mi_archivo = open(carpeta)
print("con Path: " + mi_archivo.read())



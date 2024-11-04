from pathlib import Path, PureWindowsPath


carpeta = Path("/Users/dorian/PythonProjects/cursos/python_total/day_6/prueba1.txt")

#print(carpeta.read_text())
print(carpeta.name) ## prueba1.txt
print(carpeta.suffix) ##.txt
print(carpeta.stem) ## prueba1

if not carpeta.exists():
    print("Este archvio no existe")
else:
    print("Genial!! existe")


## Para obtener la ruta en windows
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)

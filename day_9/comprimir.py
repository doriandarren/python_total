import zipfile
import shutil

mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')

mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')

mi_zip.close()


zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')
zip_abierto.extractall()



# carpeta_origen = '/Users/dorian/PythonProjects'
# carpeta_destino = '/Users/dorian/PythonProjects'
# shutil.make_archive(carpeta_destino, 'zip', carpeta_origen)
# shutil.unpack_archive('Todo_Comprimdo.zip', 'Extraxxion terminada', zip)





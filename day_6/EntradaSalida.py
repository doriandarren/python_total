mi_archivo = open('prueba.txt')


# una_linea = mi_archivo.readline()
# print(una_linea.rstrip())
#
# una_linea = mi_archivo.readline()
# print(una_linea)
#
# una_linea = mi_archivo.readline()
# print(una_linea)



# for l in mi_archivo:
#     print("Aqui dice: " + l)


## Devuelve una lista []
todas = mi_archivo.readlines()
print(todas[0])



mi_archivo.close()


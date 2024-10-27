mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
mi_lista3 = mi_lista + mi_lista2

otra_lista = ['hola', 55, 6.1]

resultado = len(mi_lista)

print(type(mi_lista))
print(resultado)


resultado = mi_lista[0:1] ## mi_lista
print(resultado)

print(mi_lista + mi_lista2)
print(mi_lista3)


mi_lista3[0] = 'alfa'
print(mi_lista3)


mi_lista3.append('g')
eliminado = mi_lista3.pop(2)

print(mi_lista3)
print(eliminado)


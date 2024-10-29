lista = ['a', 'b', 'c', 'd']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra: {letra} posicion {numero_letra}")




lista1 = ['pablo', 'laura', 'fede', 'luis', 'julia']
for nombre in lista1:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print("No comienza con L")



numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)


palabra = 'python'

for letra in palabra:
    print(letra)


# Se cargan a y b como 1 y 2, asi sucesivamente
for a,b in [[1,2], [3,4], [5,6]]:
    print(a)
    print(b)


dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}

for item in dic.items():
    print(item)


for a,b in dic.items():
    print(a, b)

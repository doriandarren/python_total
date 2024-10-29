palabra = 'python'

#lista = []
#for letra in palabra:
#    lista.append(letra)


## "letra" debe ser la misma
lista = [letra for letra in palabra]
lista2 = [letra for letra in 'python']
lista3 = [letra for letra in range(0,21,2)]

## que el resultado de los numeros se divida entre 2
lista4 = [n / 2 for n in range(0,21,2)]

# Con if
lista5 = [n for n in range(0,21,2) if n * 2 > 10]

## Con if else
lista6 = [n if n * 2 > 10 else 'no' for n in range(0,21,2) ]

print(lista)
print(lista2)
print(lista3)
print(lista4)
print(lista5)
print(lista6)


pies = [10,20,30,40,50]
metros = [p / 3.281 for p in pies]
print(metros)


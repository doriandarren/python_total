
lista = ['a', 'b', 'c']
#indice = 0

for indice, item in enumerate(lista):
    ##print(indice, item)
    ##indice += 1

    print(indice, item)



for indice, item in enumerate(range(50,55)):
    print(indice, item)


mis_tuples = list(enumerate(lista))
print(mis_tuples)
print(mis_tuples[1][0])

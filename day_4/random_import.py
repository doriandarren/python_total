from random import *

# int
aleatorio = randint(1, 50)
print(aleatorio)

# decimal
aleatorio2 = uniform(1,5)
print(aleatorio2)

aleatorio3 = round(uniform(1,5), 2)
print(aleatorio3)

# Numero aleatorio decimal
aleatorio3 = random()
print(aleatorio3)

#Elige aleatorio cualquier valor de la lista
colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio = choice(colores)
print(aleatorio)


# Mezcla los valores (no sirve para string)
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)
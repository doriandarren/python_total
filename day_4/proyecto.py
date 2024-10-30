from random import randint

intentos = 0
numero_secreto = randint(1,100)

nombre = input("Dime tu nombre: ")

estimado = 0

print(f"Bueno {nombre}, he pensado un número entre 1 y 100\nTienes 8 intentos para adivinar")

while intentos < 8:
    estimado = int(input("Cual es el número: "))
    intentos += 1

    if estimado not in range(1, 101):
        print("Tu número no esta en el rango de 1 y 100")
    elif estimado < numero_secreto:
        print("Mi número es más alto")
    elif estimado > numero_secreto:
        print("Mi número es más bajo")
    else:
        print(f"Felicitaciones {nombre}! Has adivinado en {intentos} intentos")
        break

if estimado != numero_secreto:
    print(f"Lo siento se han agotado los intentos. El número secreto era {numero_secreto}")
from random import shuffle

#Listar inicial
palitos = ['-', '--', '---', '----']


# Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista


# Pedirle intento
def probar_suerte():
    intento = ''

    while intento not in ['1', '2', '3', '4']:
        intento = input("Número del 1 al 4: ")

    return int(intento)


# comprobar intento
def comprobar_intento(lista, intento):
    if lista[intento -1] == '-':
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")

    print(f"Te hatocado {lista[intento - 1]}")



palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
comprobar_intento(palitos_mezclados, seleccion)
def mi_funcion():
    lista = []
    for x in range(1,5):
        lista.append(x*10)
    return lista


def mi_generador():
    for x in range(1, 5):
        yield x * 10




print(mi_funcion())
print(mi_generador())

g = mi_generador()

print(next(g))
print(next(g))
print(next(g))



"""
Otro ejemplo:
"""
print("*" * 20)
print("Otro ejemplo: ")

def mi_generador2():
    x = 1
    yield 1

    x += 1
    yield x

    x += 1
    yield x


g2 = mi_generador2()

print(next(g2))
print(next(g2))
print(next(g2))





def mi_generador3():
    x = "Te quedan 3 vidas"
    yield x

    x = "Te quedan 2 vidas"
    yield x

    x = "Te queda 1 vida"
    yield x

    x = "Game Over"
    yield x


perder_vida = mi_generador3()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
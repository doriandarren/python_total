def suma(*args):
    # total = 0
    # for arg in args:
    #     total += arg
    # return total

    return sum(args)

print(suma(5,4,3,4,50,32))



#
# Ejemplo de for en una sola linea
#
def suma_cuadrados(*args):
    return sum((arg ** 2) for arg in args)

print(suma_cuadrados(1, 2, 3))



#
## For en una sola linea
#
def suma_absolutos(*args):
    return sum(abs(x) for x in args)


print(suma_absolutos(1, 5, 4, -10))





def numeros_persona(nombre, *args):
    suma_numeros = sum(args)

    return f"{nombre}, la suma de tus números es {suma_numeros}"


print(numeros_persona("Jose", 3, 4, 10, 3))
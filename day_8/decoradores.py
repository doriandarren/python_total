"""
Decoradores
"""
def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')

    return otra_funcion


def mayuscula_decorador(texto):
    print(texto.upper())

@decorar_saludo
def minuscula_decorador(texto):
    print(texto.lower())


minuscula_decorador("Python")






"""
Funciones dentro de funcion
"""
def mayuscula(texto):
    print(texto.upper())


def minuscula(texto):
    print(texto.lower())


def una_funcion(funcion):
    return funcion


## Alacenar una funcion en variable
mi_funcion = mayuscula
mi_funcion("pytohn")


## Pasar funcion como parametro:
una_funcion(mayuscula("probando"))








"""
Funciones dentro de función
"""
def camiar_letras(tipo):
    def mayuscula_interna(texto):
        print(texto.upper())

    def minuscula_interna(texto):
        print(texto.lower())

    if tipo == 'may':
        return mayuscula_interna
    elif tipo == 'min':
        return minuscula_interna


operacion = camiar_letras('may')
operacion("hola")




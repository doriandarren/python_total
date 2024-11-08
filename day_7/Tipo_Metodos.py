class Pajaro:

    alas = True

    # Constructor
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


    # Métodos de Instancia
    def piar(self):
        print("pio")

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pájaro es {self.color}")



    # Métodos de clase
    # No necesita instancias
    # no puede acceder a las propieddes de la clase

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")

        ## Error - No se puede hacer
        ## print(f"Es color {self.color}") ###----

        ## Con "cls" este si
        cls.alas = False
        print(Pajaro.alas)


    @staticmethod
    def mirar():

        # Error
        # self.color = 'Negro'
        # cls.alas = 2

        # No da error porque no tiene nada que ver con los metodos ni atributos de la clase
        print("El pajaro mira")



##
## Llamadas para metodos de instancia
##
# piolin = Pajaro("amarillo", "canario")
# piolin.volar(50)
# piolin.alas = False
# print(piolin.alas)



##
## Llamadas para metodos de clase
## No necesita instancias
##
Pajaro.poner_huevos(3)



##
## Llamadas staticos
## No necesita instancias

Pajaro.mirar()



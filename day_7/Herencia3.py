class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("ja ja ja")

    def habla(self):
        print("Que tal!!")


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass



mi_nieto = Nieto()
mi_nieto.hablar()
## mi_nieto.reir()

print(Nieto.__mro__) ## (mro: Method Order Resolution) Imprime el order de resolucion de los metodos heredados
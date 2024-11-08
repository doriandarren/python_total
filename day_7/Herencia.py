class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color


    def nacer(self):
        print("Este animal ha nacido")



class Pajaro(Animal):
    pass




print(Pajaro.__bases__) ## Imprime su Padre
print(Animal.__subclasses__()) ## Imprime sus hijas



piolin = Pajaro(2, 'amarillo')
piolin.nacer()


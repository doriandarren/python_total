class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color


    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emiyte sonido")


class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("Pio")

    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")




piolin = Pajaro(3, 'amarillo', 60)
piolin.hablar()
piolin.volar(300)


mi_animal = Animal(5, 'negro')



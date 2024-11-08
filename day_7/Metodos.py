class Pajaro:

    alas = True

    # Constructor
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("pio")

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")



piolin = Pajaro("amarillo", "canario")
piolin.piar()
piolin.volar(45)


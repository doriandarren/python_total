class Pajaro:

    def __init__(self, color, especie):
        self.color = color
        self.espacie = especie

    def piar(self):
        print(f"pio, mi color es {self.color}")

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")


piolin = Pajaro("amarillo", 'canario')
piolin.volar(50)
piolin.piar()

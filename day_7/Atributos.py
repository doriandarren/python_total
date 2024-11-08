class Pajaro:

    alas = True

    # Constructor
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie




mi_pajaro = Pajaro("Blanco", "Tucan")

# print(mi_pajaro.color)
# print(mi_pajaro.especie)


print(f"mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")
print(Pajaro.alas)
print(mi_pajaro.alas)
import numeros


def preguntar():

    print("Bienvenido a farmacoa Python")

    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmetica")

        try:
            mi_rubro = input("Elija su opción: ").upper()
            ["P", "F", "C"].index(mi_rubro)
        except ValueError:
            print("Opción no válida")
        else:
            break

    numeros.decorador(mi_rubro)


def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("Quieres otro turno? [S/N]").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Opción no válida")
        else:
            if otro_turno == 'N':
                print("Gracias por su visita")
                break


inicio()
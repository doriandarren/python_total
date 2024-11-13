
def sumar():
    n1 = int(input("número 1: "))
    n2 = int(input("número 2: "))
    print(n1 + n2)
    print("Gracias por sumar")


try:
    # código
    sumar()
except TypeError:
    # error
    print("Estas concatenando tipos diferentes")
except ValueError:
    # error
    print("Ese no es un numero")
else:
    # Codigo sino hay error
    print("Hiciste todo bien")
finally:
    # Finalmente
    print("Eso fue todo")



def pedir_numero():

    while True:
        try:
            numero = int(input("número 1: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break

    print("gracias")


pedir_numero()
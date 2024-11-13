def suma(**kwargs):
    #print(type(kwargs))

    total = 0

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor} ")
        total += valor

    return total

print(suma(x=3, y=5, z=2))







def suma_nueva(num1, num2, *args, **kwargs):
    print(f"El primer valor es: {num1}")
    print(f"El segundo valor es: {num2}")



    for arg in args:
        print(f"arg: {arg}")


    for clave,valor in kwargs.items():
        print(f"{clave} = {valor} ")

## De esta manera:
suma_nueva(15, 50,245,3,4,54,33,432, x=3, y=5, z=2)



## De esta otra:
lista_args = [245,3,4,54,33,432]
dic_kwargs = { "x": 3, "y": 5, "z":2 }

suma_nueva(15, 50,*lista_args, **dic_kwargs)


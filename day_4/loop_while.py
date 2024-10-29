
monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas = monedas - 1
else: print("No tengo más dinero...")



respuesta = 's'

while respuesta == 's':
    respuesta = input("quieres seguir? (s/n): ")
else:
    print("Hasta luego...")
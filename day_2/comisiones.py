

nombre = input("Por favor en nombre: ")
ventas = int(input("Sus ventas del mes: "))

comision = round(ventas * 13 / 100, 2)


print(f"Hola {nombre} tus comisiones de este mes ${comision}")
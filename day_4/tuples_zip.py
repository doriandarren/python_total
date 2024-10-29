nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65,29,42, 55]
ciudades = ['Lima', 'España', 'Mexico']

combinados = list(zip(nombres, edades, ciudades))
print(combinados)

for nombre,edad,cuidad  in combinados:
    print(f"{nombre} tiene {edad} años y vivi {cuidad}")
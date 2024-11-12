
precios_cafe = [('capuchino', 1.5), ('Expresso', 1.2), ('Moka', 3.9)]

def buscar_mas_caro(lista_precio):
    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe,precio in lista_precio:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro, precio_mayor)



cafe, precio = buscar_mas_caro(precios_cafe)
print(f"El cafe más caro es: {cafe} y el precio es: {precio}")
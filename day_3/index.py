
mi_texto = "Esta una prueba"
resultado = mi_texto[0]
## resultado2 = mi_texto.index("prueba")
resultado2 = mi_texto.index("a", 5, len(mi_texto)) ##

resultado3 = mi_texto.rindex("a") ## buscar al reves


print(resultado)
print(resultado2)
print(resultado3)
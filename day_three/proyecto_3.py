## Anilizador de letras

## uno no es lo que es por lo que escribe, sino por lo que ha leído

texto = input("Texo: ")
letras = []

texto = texto.lower()

letras.append(input("Primera leta: ").lower())
letras.append(input("Segunda leta: ").lower())
letras.append(input("tercera leta: ").lower())

print("\n")
print("Cantidad de letras")
cantidad_letas1 = texto.count(letras[0])
cantidad_letas2 = texto.count(letras[1])
cantidad_letas3 = texto.count(letras[2])

print(f"Hemos encontrado la letra {letras[0]} repetidas {cantidad_letas1} veces")
print(f"Hemos encontrado la letra {letras[1]} repetidas {cantidad_letas2} veces")
print(f"Hemos encontrado la letra {letras[2]} repetidas {cantidad_letas3} veces")

print("\n")
print("Cantidad de palabras")
palabras = texto.split()
print(f"Se encontró {palabras} palabras en tu texto")

print("\n")
print("Letra inicio y fin")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"Incial: {letra_inicio} y fin {letra_final}")



print("\n")
print("Texto invertido")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Invertido: {texto_invertido}")


print("\n")
print("Texto Python")

buscar_python = 'python' in texto
dic = {True:"si", False:"no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")


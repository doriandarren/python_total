# r: solo lectura
# w: hace que se regenere por completo
# a: escribe al final del archivo

file = open("prueba1.txt", 'w')

file.write("Soy un nuevo texto\n")
file.write("Hola\n")
file.write("Mundo")

file.write('''Hola
de nuevo 
con 
salto de
linea con comillas triples
''')

## No se usa casi
file.writelines(['\nHola\n', 'mundo\n', 'aqui\n', 'estoy\n'])

file.close()
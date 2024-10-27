
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5] ## desde la posicion 2 hasta el 5 (no incluido el 5) CDE
fragmento1 = texto[2:] ## desde la posicion 2 hasta el fin
fragmento2 = texto[:5] ## hasta la posicion 5
fragmento3 = texto[::2] ## Brinca de 2 en 2 completa la cadena hacia adelante
fragmento4 = texto[::-2] ## Brinca de 2 en 2 completa la cadena hacia atras de retroceso



print(fragmento)
print(fragmento1)
print(fragmento2)
print(fragmento3)
print(fragmento4)
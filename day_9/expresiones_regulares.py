
"""
carcteres       descripcion                 Ejemplo         Lo que se puede mostrar
\d              digito numero   ->          v.\d.\d\d       v1.02 v1.03 v1.01 etc
\w              caracter alfanumerico       \w\w\w-\w\w     sol-do abac-25 ABC-25 Nro-al
\s              espacio en blanco           numero\s\d\d    número 25 / número 01 / número 99 / etc

Los mismos en mayusculas significa que tiene en el efecto contrario:
\D              NO es numerico              \D\D\D\D        accd / AbCd / AB-C / abc?
\W              NO es alfanumerico          \W\W\W          +=- / ??? / ¡*! / ###
\S              NO es espacio en blanco     \S\S\S\S        1234 / abcd / ¿si? / v.A1

Cuantificadores: (no se tenga que repetir )

+               1 ó más veces               código_\d-\d+   código_5-5 / código_5-555 / código_1-02 / código_9-99944
{n}             se repite n veces           \d-\d{4}        1-0000 / 1-2334 / 5-7777 / 8-0001
{n,m}           se repite de n a m veces    \w{3-5}         hola / sol / mundo / yo6789
{n,}            desde n hacia infinito      -\d{4,}         -11111111- / -5432- / -000590585847585950- / -000000-
*               0 ó más veces               \w\s*\w         a 2 / a     b / fm / s4
?               1 ó 0                       casas?          casa / casas
"""


import re
from re import search

texto = "Si necesitas ayuda llama al (685)-598-9887 las 24 horas al servicio de ayuda online"

#palabra = 'ayuda' in texto
#print(palabra)


patron = 'ayuda' # 'nada'

busqueda = re.search(patron, texto)
print(busqueda)
print(busqueda.span())
print(busqueda.start())
print(busqueda.end())



busqueda = re.findall(patron, texto)
print(len(busqueda))


for encontro in re.finditer(patron, texto):
    print(encontro.span())



texto = 'llama al 567-345-7896 ya mismo'

patron = r'\d{3}-\d{3}-\d{4}' # ó asi:  r'\d\d\d-\d\d\d-\d\d\d\d'
resultado = re.search(patron, texto)
print(resultado)
print(resultado.group())


patron = r'(\d{3})-(\d{3})-(\d{4})' # si se encierra en parentesis los agrupa para luego con el indice se imprime
resultado = re.search(patron, texto)
print(resultado.group(2))


# clave = input("clave: ")
# patron = r'\D{1}\w{7}'
# chequear = re.search(patron, clave)
# print(chequear)


texto = 'No atendemos los lunes por la tarde'
buscar = re.search(r'lunes|martes', texto)
print(buscar)


texto = 'No atendemos los lunes por la tarde'
buscar = re.search(r'....demos...', texto)
print(buscar)
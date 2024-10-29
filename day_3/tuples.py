mi_tuple = (1,2,3,4)

print(type(mi_tuple))
print(mi_tuple[-2]) ## de derecha a izquierda

#Error
# mi_tuple[0] = 5
# print(mi_tuple)

mi_tuple1 = (1,2,(20,40),4)
print(mi_tuple1[2][0])

mi_tuple1 = list(mi_tuple1)
mi_tuple1 = tuple(mi_tuple1)

print(mi_tuple1)

t = (1,2,3)
x,y,z = t ##Parecido a desestructurar pero tienen que tener la misma cantidad de elementos

print(x,y,z)


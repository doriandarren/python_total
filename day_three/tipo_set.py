mi_set = set([1,2,3,4,5])

print(type(mi_set))
print(mi_set)


otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)

print(len(otro_set))


s1 = {1,2,3}

s1.add(2)

s2 = {3,4,5}
s2.remove(5)
s2.discard(8)
s2.pop() ## Elimina elemento aleatorio

s2.clear() ## limpia el set

s3 = s1.union(s2)
print(s3)



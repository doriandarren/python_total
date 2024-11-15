from collections import Counter, defaultdict, namedtuple

numeros = [8,4,3,4,4,6,6,6,7,5,3,9]

print(Counter(numeros))

print(Counter('mississipi'))

frase = 'al pan pan y al vino vino'
print(Counter(frase.split()))

serie = Counter(numeros)
print(serie.most_common())



mi_dic = {'uno': 'verde', 'dos': 'azul', 'tres': 'rojo'}

## print(mi_dic['cuatro']) ## Error


mi_dic_lambda = defaultdict(lambda: 'nada')
mi_dic_lambda['uno'] = 'verde'
print(mi_dic_lambda['dos'])


Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 79)

print(ariel.altura)
print(ariel[2])
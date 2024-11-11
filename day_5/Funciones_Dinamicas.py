
def busca_3_cifras(numero):
    return numero in range(100, 1000)

def busca_lista_3_cifras(lista):

    lista_3_cifras = []

    for n in lista:
        if n in range(100, 1000):
            ##return True
            lista_3_cifras.append(n)
        else:
            pass

    return lista_3_cifras


# resultado = busca_3_cifras(65)
# print(resultado)


resultado = busca_lista_3_cifras([552, 99, 90349, 444])
print(resultado)
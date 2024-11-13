def ceros_vecinos(*args):

    contador = 0

    for num in args:

        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1 ] == 0:
            return True
        else:
            contador += 1

    return False


print(ceros_vecinos(0,5,6,7,7,5,0,0,4,3,2,4,34,3,0))
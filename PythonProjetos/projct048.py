s = 0
n = 0
for c in range(0,501,3):
    if c/2%1 != 0:
        s += c
        n += 1
print('\033[0;34mSOMA DE TODOS OS {} NUMEROS'.format(n))
print('PARES, MULTIPLOS DE 3 QUE ESTAO ENTRA 1 E 500 E \033[4;31m{}.'.format(s))

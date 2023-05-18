s = 0
t = 0
for c in range(1,7):
    n = int(input('\033[0;33mDIGITE O {} NUMERO AQUI: '.format(c)))
    if n/2%1 == 0:
        s += n
        print('PAR...')
        t += 1
    else:
        print('IMPAR...')

print('\033[0;34mA soma dos {} numeros pares  digitados SAO \033[0;31m{}.'.format(t,s))
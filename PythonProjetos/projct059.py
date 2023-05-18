c = 0
from time import sleep
ama = ('\033[0;33m')
ver =  ('\033[0;32m')
num = float(input('\033[0;34mPrimeiro valor: '))
num1 = float(input('Segundo valor: '))
while c == 0:
    print('''\033[0;33m    [ 1 ] = Soma.
    [ 2 ] = Multiplicação.
    [ 3 ] = Maior.
    [ 4 ] = Novos Numeros.
    [ 5 ] = Sair do progama.''')
    opç = int(input('»»{}Opção do Menu: '.format(ver)))
    if opç == 1:
        print('SOMA = {}{} + {} = {}'.format(ver,num,num1,num+num1))
    elif opç == 2:
        print('MULTIPLICAÇÃO = {}{} . {} = {}'.format(ver,num,num1,num*num1))
    elif opç == 3:
        if num < num1:
            print('MAIOR = {}{} E o maior.'.format(ver,num1))
        else:
            print('MAIOR = {}{} E o maior.'.format(ver,num))
    elif opç == 4:
        num = float(input('{}Primeiro valor: '.format(ama)))
        num1 = float(input('{}Segundo valor: '.format(ama)))
    elif opç == 5:
        print('FECHANDO PROGAMA',end='')
        for c in range(5,0,-1):
            sleep(0.5)
            print('.',end='')
        print('FECHADO.')
        exit()

    else:
        print('\n\033[0;31mOPÇÃO INVALIDA.')
    print('=-='*15)
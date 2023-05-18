n1 = int(input('\033[0;33mPrimeiro Numero Inteiro, Digite Aqui: '))
n2 = int(input('Segundo Numero Inteiro, Digite Aqui: '))
if n1 > n2:
    print('\033[0;32mO PRIMEIRO valor e maior....')
elif n2 > n1:
    print('\033[0;34mO SEGUNDO valor e maior...')
else:
    print('\033[0;31mNÃO EXISTE valor maior, ambos sao iguais....')



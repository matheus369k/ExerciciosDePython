esc = 0
cor = '\033[0;32m'
while True:
    num = int(input('\033[0;33mTABUADA DE QUAL VALOR (NUMERO NEGATIVO PARA PARAR): '))
    if num < 0:
        break
    print('\033[0;34m[ x ] = 1.\n[ - ] = 2.\n[ \ ] = 3.\n[ + ] = 4. ')
    esc = int(input('\033[0;33mOpçao: '))
    for c in range(1, 11):
        if esc == 1:
            print(f'{cor}{num} x {c} = {num*c}.')
        elif esc == 2:
            print(f'{cor}{num} - {c} = {num-c}.')
        elif esc == 3:
            print(f'{cor}{num} \ {c} = {num/c:.1f}.')
        elif esc == 4:
            print(f'{cor}{num} + {c} = {num+c}.')
        else:
            print('\033[0;31mOPÇÃO INVALIDA!')
print('\033[0;34mProgama encerrado!')
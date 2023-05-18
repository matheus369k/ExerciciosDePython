print(' '*43,'\033[0;34m< TABUADA AVANÇADA >\n')
print('\033[0;33m( 1 ) = Tabuada base.\n( 2 ) = Tabuada avançada.')
escolha = int(input('Digite aqui sua escolha: '))
print('='*30)
if escolha == 1:
    num = int(input('\033[0;32mPRIMEIRO NUMERO:'))
    fim = int(input('SEGUNDO NUMERO: '))
    print('='*30)
    for c in range(1,fim+1,1):
        n = num/c
        n1 = num+c
        n2 = num-c
        n3 = num*c
    print('\033[0;31m{} / {} = {:.2f}'.format(num,fim,n))
    print('{} + {} = {}'.format(num,fim,n1))
    print('{} - {} = {}'.format(num,fim,n2))
    print('{} . {} = {}'.format(num,fim,n3))
elif escolha == 2:
    inic = int(input('\033[0;34mINICIO DA TABUADA: '))
    fim = int(input('FIM DA TABUADA: '))
    num = float(input('NUMERO A SER CALCULADO: '))
    print('='*30)
    print('\033[0;33m( 1 ) = ( + )\n( 2 ) =  ( - )\n( 3 ) = ( / )\n( 4 ) = ( . ).')
    escolha2 = int(input('OPÇÃO AQUI:'))
    print('='*30)
    for c in range(inic,fim+1):
        if escolha2 == 1:
            print('\033[0;31m{} + {} = {:.2f}.'.format(c,num,c + num))
        elif escolha2 == 2:
            print('\033[0;31m{} - {} = {:.2f}.'.format(c,num,c - num))
        elif escolha2 == 3:
            print('\033[0;31m{} / {} = {:.2f}.'.format(c,num,c // num))
        elif escolha2 == 4:
            print('\033[0;31m{} . {} = {:.2f}'.format(c,num,c * num))
        else:
            print('\033[0;31mOPÇÃO INVALIDA.....')
else:
    print('\033[0;31mOPÇÃO INVALIDA.....')




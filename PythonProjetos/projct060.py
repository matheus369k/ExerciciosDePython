num = int(input('\033[0;33mDigite o valor: '))
print('( 1 ) = While.\n( 2 ) = For.')
escolha = int(input('OPÇÃO:'))
if 1 == escolha:
    s = num
    t = 0
    print('\033[0;31m{}! FATORIAL...COM (While)...'.format(num))
    print('\033[0;34m==='*10)
    while num != 1 :
        num -= 1
        s *= num
        if s == num*(num+1) :
            print('\033[0;32m{} . {} = {}'.format(num+1,num,s))
        else:
            print('\033[0;32m{} . {} = {}'.format(num,t,s))
        t = s
    print('\33[0;34m==='*10)
elif 2 == escolha:
    print('\033[0;31m{}! FATORIAL......COM (For)....'.format(num))
    to = num
    t = 0
    for c in range(num,1,-1):
        num *= (c-1)
        if c == to:
            print('\033[0;32m{} . {} = {}'.format(to,c-1,num))
        else:
            print('\033[0;32m{} . {} = {}'.format(c-1,t,num))
        t = num
    print('\033[0;34m==='*10)
else:
    print('\033[0;31mSO HA 2 OPÇÕES......')
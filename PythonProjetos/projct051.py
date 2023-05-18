print(' '*40,'\033[0;34mRAZÃO P.A\n')
inc = int(input('\033[0;32mINICIO DA PROGUEÇÃO: '))
fim = int(input('FIM DA PROGUEÇÃO: '))
pa = int(input('TERMO DA RAZÃO: '))
for c in range(inc,fim+1,pa):
    print('\033[0;33m{}'.format(c),'-> ',end='')
print('\033[4;31mEND.')
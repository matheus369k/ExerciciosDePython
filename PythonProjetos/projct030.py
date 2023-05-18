print(' '*45,'\033[0;35m=+='*6)
print(' '*45,'<= Par OU Impar','=>')
print(' '*45,'=+='*6)
num = int(input('digite o numero aqui: '.title()))
num1 = num/2%1
if num1 == 0:
    print('\033[0;36m<=>'*9)
    print('\033[0;32m<=  O NUMERO {} E PAR!!!  =>'.format(num))
    print('\033[0;36m<=>'*9)
else:
    print('\033[0;35m<=>'*10)
    print('\033[0;33m<=   O NUMERO {} E IMPAR!!   =>'.format(num))
    print('\033[0;35m<=>'*10)

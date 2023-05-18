print(' '*40,'\033[0;31m< MAIOR DE 21 ANOS. >')
from datetime import date
n = 0
s = 0
for c in range(1,8):
    ano = int(input('\033[0;33mANO DE NASCIMENTO A {}° PESSOA: '.format(c)))
    atual = date.today().year
    idade = atual-ano
    if idade >= 21 :
        s = s+1
    else:
        n = n+1
print('\033[0;34m{} SAO MENORES DE 21 ANOS......'.format(n))
print('{} SAO MAIORES DE 21 ANOS.......'.format(s))



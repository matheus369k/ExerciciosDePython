from random import randint
n  = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print('\033[0;31m§=§'*15)
print(f'\033[0;36mOS Numeros escolhidos foram',end=' ')
for c in n:
    print(f'{c}',end=' ')
print('\n',end='')
print('\033[0:31m§=§'*15)
print(f'\033[0;36mO MENOR numero escolhido pelo PC foi {min(n)}.')
print(f'O MAIOR numero escolhido pelo PC foi {max(n)}.')
print('\033[0;31m§=§'*15)

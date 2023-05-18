limpa = '\033[m'
cores = '\033[0;32m'
print(' '*30,cores,'>=-='*7,'>',limpa)
print(' '*30,cores,'<   NUMERO MAIOR E MENOR!!   >',limpa)
print(' '*30,cores,'>=-='*7,'>',limpa)
n1 = int(input('\n{}primeiro numero, digite aqui: '.format(cores)))
n2 = int(input('segundo numero, digite aqui: '))
n3 = int(input('terceiro numero, digite aqui:{} '.format(limpa)))
#Verificar o menor numero
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#verificar o maior numero
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('\n{}O MAIOR NUMERO E O {}.{}'.title().format(cores,maior,limpa))
print('{}O MENOR NUMERO E O {}.{}'.title().format(cores,menor,limpa))


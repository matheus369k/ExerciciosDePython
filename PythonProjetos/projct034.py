limpa = '\033[m'
cores = '\033[0;30;42m'
print(' '*30,cores,'>=-='*7,'>',limpa)
print(' '*35,cores,'<  Salario Aumento  >',limpa)
print(' '*30,cores,'>=-='*7,'>',limpa)
valor = int(input('\n\033[0;30;42mvalor do salario digite aqui:\033[m \n'))
if 1250 <= valor:
    taxa = '10%'
    aumento = ((valor*10)/100)+valor
else:
    taxa = '15%'
    aumento = ((valor*15)/100)+valor
print('{}Com o salario de {}R$  e tendo um aumento de {}, fica com o salario final em {}R${}'.format(cores, valor, taxa, aumento, limpa))
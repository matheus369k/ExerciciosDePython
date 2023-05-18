print('\nalmentando o preço por porcentagem.')
porcentagem = float(input('Digite o valor da porcentagem aqui,(SEM 0 SIMBOLO): '))
preço = float(input('Digite o valor do preço aqui:R$ '))
almento = (preço * porcentagem) / 100
n_preço = preço + almento
print('Tendo um preço de R${} e com o aumento de {}%'.format(preço, porcentagem))
print('acaba por ficar  R${:.2f} com o bonos de R${:.2f}.'.format(n_preço, almento15))

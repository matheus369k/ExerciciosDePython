print('\nTira descontos com porcentagem.')
porcentagem = float(input('Digite aqui a porcentagem, (sem o simbolo):'))
preço = float(input('Digite o valor a ser descontado aqui:R$'))
n_preço = (porcentagem * preço) / 100
a_preço = preço - n_preço
print('O preço inicial sendo R${} que teve um desconte de {}%,'.format(preço, porcentagem))
print('acaba por ter um desconto de R${:.2f} e ficando com preço final de R${:.2f}.'.format(n_preço, a_preço))

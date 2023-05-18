print('\nConverter Reais em Dollar!!!.')
valor = float(input('Digite o valor em reais aqui:R$'))
dollar = valor / 3.27
print('Com R${} vc consegui comprar U${:.1f}.'.format(valor, dollar))

print('\nCalcular quantidade de tinta para pintar uma parede.')
altura = float(input('A altura da parede: '))
largura = float(input('A largura da parede: '))
area = altura * largura
tinta = area / 2
print('Uma parede de Area igual a {:.2f}m² voce precisa de {:.2f}L de tinta'.format(area, tinta))

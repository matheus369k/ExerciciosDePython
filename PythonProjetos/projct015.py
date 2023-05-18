print('\naluguel de um carro.')
taxa_fixa = float(input('valor fixo do aluguel do carro:R$'))
taxa_km = float(input('Quantida a pagar por km percorrido:R$'))
km = float (input('Quantidade de km percorridos:km '))
total = taxa_fixa + (taxa_km * km)
print('quantidade a pagar:\nPreço fixo R${}\nvalor por km percorrido R${} '.format(taxa_fixa, taxa_km))
print('ultilizado por {}km.\no valor total a ser pago e {}R$'.format(km, total))


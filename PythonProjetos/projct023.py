print('atençao so aceitaos numeros interios e de 0 a 9999'.title())
numero = input('digite o numero desejado aqui: '.title())
print('{} = unidade.\n{} = dezena.'.title().format(numero[3],numero[2]))
print('{} = centena.\n{} = milhar.'.title().format(numero[1],numero[0]))
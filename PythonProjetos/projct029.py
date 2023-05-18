print(' '*37,'\033[0;34m<=>'*12)
print(' '*37,'<  Multa Por Ultrapaçar Limite!!!  >')
print(' '*37,'<=>'*12)
km = float(input('quantos Km/H voce chegou? '))
multa = (km-80)*7
if km > 80:
    print('\033[4;31mvoce ultrapaçou o limite de 80km/h .')
    print('tendo isso em conta vc recebera uma multa de 7R$, por cada km/h acima de 80'.title())
    print('voce tera que pagar {:.2f}R$'.format(multa))
print('\033[0;32mtenha um bom dia, dirija com segurançao.')
from datetime import date
ano = int(input('\033[0;32mDIGITE AQUI...Seu Ano de Nascimento:'))
atual = date.today().year
new = atual-ano
print('\033[0;33mIDADE DO ATLETA: {}\033[0;34m'.format(new))
if new <= 9:
    print('CATEGORIA: MIRIM.')
elif new <= 14:
    print('CATEGORIA: INFANTIL.')
elif new <= 19:
    print('CATEGORIA: JUNIOR.')
elif new <= 25:
    print('CATEGORIA: SENIOR.')
else:
    print('CATEGORIA: MASTER.')
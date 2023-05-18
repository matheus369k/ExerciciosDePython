num = c = n = maior = menor = 0
op = ''
while op != 'N':
    c += 1
    num = int(input('\033[0;34m{}° Valor: '.format(c)))
    op = str(input('\033[0;33mQuer continuar digitando numeros? S/N: ')).upper()
    n += num
    if  c == 1:
        maior = menor = num
    elif maior < num:
        maior = num
    elif menor > num:
        menor = num
print('\033[0;32mNUMEROS DIGITADOS: {}.'.format(c))
print('MEDIA: {:.2f}.\nMAIOR: {}.\nMENOR: {}.'.format((n/c),maior,menor))

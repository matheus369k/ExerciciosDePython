num = n = c = 0
print('\033[0;36mDigite [ 999 ] para parar.')
while num != 999:
    c += 1
    num = int(input('\033[0;33m{}° Valor:'.format(c)))
    if num != 999:
        n += num
print('\033[0;32mForam digitados {}  numeros, sendo sua soma igual a {}.'.format(c-1,n))


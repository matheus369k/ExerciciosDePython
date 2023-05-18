list = []
dado = []
az = '\033[;36m'
while True:
    print(f'{az}§=§' * 15)
    dado.append(str(input('\033[;33mNOME: ')))
    dado.append(float(input('\033[;33mPESO: ')))
    list.append(dado[:])
    dado.clear()
    cont = str(input('\033[;33mQuer continuar? [S/N]: '))
    while cont not in 'sSnN':
        cont = str(input('\033[;33mQuer continuar? [S/N]: '))
    if cont in 'nN':
        break
print(f'{az}§=§'*15)
print(f'\033[;32mAo todo, você cadrastou {len(list)} pessoas.')
cont = 0
for c in list:
    if cont == 0:
        pesado = c[1]
        pena = c[1]
    if  c[1] > pesado:
        pesado = c[1]
    if  c[1] < pena:
        pena = c[1]
    cont += 1

print(f'\033[;32mO maior peso foi  de {pesado}kg. Peso de ',end='')
for c in list:
    if c[1] == pesado:
        print(c[0],end=' ')
print('.')
print(f'\033[;32mO menor peso foi de {pena}kg. Peso de ',end='')
for c in list:
    if c[1] == pena:
        print(c[0],end=' ')
print('.')
print(f'{az}§=§'*15)

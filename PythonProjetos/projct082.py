list = []
par = []
imp = []
d = 0
az = '\033[;36m'
print(f'{az}§=§'*15)
while True:
    print(f'\033[;31mVALOR {d}.')
    list.append(int(input('\033[;33mDigite um valor: ')))
    es = str(input('\033[;33mQuer continuar: [S/N]')).lower().strip()[0]
    while es not in 'sn':
        es = str(input('\33[;33mQuer continuar: [S/N]')).lower().strip()[0]
    if es == 'n':
        break
    d += 1
    print(f'{az}§=§'*15)
for c in range(0,len(list)):
    if list[c] % 2 == 0:
        par.append(list[c])
    else:
        imp.append(list[c])
print(f'{az}§=§'*15)
print(f'\033[;32mA lista completa e {list}!')
print(f'A lista de pares e {par}!')
print(f'A lista de impares e {imp}!')
print(f'{az}§=§'*15)
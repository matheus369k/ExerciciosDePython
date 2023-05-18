reg = []
while True:
    print('\033[;36m-'*21,'\033[;32mREGISTO','\033[;36m-'*21)
    print('\033[;32m')
    dtemp = {'NOME':str(input('Nome: ')).title()}
    s = str(input('Sexo [M/F]:')).title()[0]
    while s not in 'MmfF':
        print('\033[;31mERRO!,Tente novamente apenas M OU F.\033[;32m')
        s = str(input('Sexo [M/F]:')).title()[0]
    dtemp ['SEXO'] = s
    dtemp ['IDADE'] = int(input('Idade:'))
    reg.append(dtemp.copy())
    dtemp.clear()
    print('\033[;36m-\033[;33m' *51)
    cont = str(input('Quer continuar?[S/N]:'))[0]
    while cont not in 'SsNn':
        print('\033[;31mERRO!,Tente novamente apenas S OU N.\033[;33m')
        cont = str(input('Quer continuar? [S/N]: '))[0]
    if cont in 'Nn':
        break
print('\033[;36m-'*13,'\033[;32minformaçao de registos','\033[;36m-'*14)
print('\033[;32m')
print(f'- O grupo tem {len(reg)} pessoas registadas.')
m =  0
h = 2
for c in reg:
    t = 0
    for v in c.values():
        if t == h:
            m += v
        t += 1

m = m/len(reg)
print(f'- A media de idade e de {m:.0f} anos.')
print('- As mulheres registadas foram: ',end='')
t = 0
for c in reg:
    for v in c.values():
        if v == 'f' or v == 'F':
            print(f'{reg[t]["NOME"]}',end=' ')
    t += 1
print('.')
t = 0
h = 2
cont = 0
print(f'- Tabela abaixo das pessoas que estao acima da media: ')
print()
print('\033[;36m-'*10,f'\033[;32mTabela de pessoas acima de {m:.0f}','\033[;36m-'*10)
print(f'\033[;31m{"NOME":<15}{"SEXO":<10}{"IDADE"}')
print('\033[;36m-'*51,'\033[;32m')
for c in reg:
    for k,v in c.items():
        if t == h and v > m:
            print(f'{reg[cont]["NOME"]:<15}{reg[cont]["SEXO"]:<10}{v}')
        t += 1
    cont += 1
    t = 0
print('\033[;36m-'*16,'\033[;31mPROGAMA ENCERRADO','\033[;36m-'*16)


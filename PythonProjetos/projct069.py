print('\033[0;34m=========Registro Pessoal========')
b = '---'*10
v = '\033[0;31m'
idade = int(input('\033[0;33mIdade:'))
sexo = str(input('Sexo: [M/F]')).lower()
h = idm = ho = md = 0
while True:
    h += 1
    if h > 1:
        if cont == 'n':
            break
        idade = int(input('\033[0;33mIdade:'))
        sexo = str(input('Sexo: M/F:')).lower().strip()[0]
    while 'f' != sexo != 'm':
        print('\033[0;31mOPÇÃO INVALIDA!')
        sexo = str(input('\033[0;33mSexo: [M/F]')).lower().strip()[0]
    cont = str(input('Quer continuar? [S/N]')).lower().strip()[0]
    while 'n' != cont != 's':
        print('\033[0;31mOPÇÃO INVALIDA!')
        cont = str(input('\033[0;33mQuer continuar? [S/N]')).lower().strip()[0]
    if idade > 18:
        idm += 1
    if sexo == 'm':
        ho +=1
    if idade < 20 and sexo == 'f':
        md += 1
    print(f'\033[0;34m{h}°REGISTRO.')
    print(v,b)
print(f'\033[0;32m{idm} Acima dos 18 anos.')
print(f'{ho} Individuo(s) de sexo Masculino.')
print(f'{md} Individuo(s) do sexo Feminino abaixo dos 20 anos.')
print(v,b)
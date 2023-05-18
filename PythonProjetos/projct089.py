dado = []
daco = []
while True:
    print('\033[;31m§§§' * 15)
    nome = str(input('\033[;33mNOME: '))
    nota1 = float(input('NOTA 1: '))
    nota2 = float(input('NOTA 2: '))
    dado.append(nome)
    dado.append(nota1)
    dado.append(nota2)
    media = (nota1 + nota2) / 2
    dado.append(media)
    daco.append(dado[:])
    dado.clear()
    print('\033[;31m---'*15)
    cont = str(input('\033[;33mQuer continuar? [S/N]'))[0]
    while cont not in 'sSnN':
        cont = str(input('\033[;33mQuer continuar? [S/N]'))[0]
    if cont in 'Nn':
        break
cont = 0
print(f'\033[;32m{"N0.":<4}{"NOME":<13}{"MÉDIA"}')
print('\033[;31m---'*15)
for c in daco:
    print(f'\033[32m{cont:<4}{c[0]:<13}{c[3]:.1f}')
    cont +=1
while True:
    print('\033[;31m---'*15)
    cha = int(input('\033[;33mMostrar notas de qual aluno? (999 interrompe): '))
    while cha > len(daco) and cha != 999 :
        cha = int(input('\033[;33mMostrar notas de qual aluno? (999 interrompe): '))
    if cha < len(daco):
        print('\033[;31m---'*15)
        print(f'\033[;32mNotas de {daco[cha][0]} são {daco[cha][1:3]}.')
    elif cha == 999:
        break
print('\033[;31m§§§'*15)
print('\033[;32mVOLTE SEMPRE!')
ddo = []
t = 0
while True:
    print('\033[;36m-'*19,'\033[;33mCOLETA DE IMFORMAÇÕES','\033[;36m-'*18)
    print('\033[;33m')
    jogado = {'NOME':str(input('Nome do Jogador: ')).title()}
    part = []
    pt = int(input(f'Quantas partidas o jogador {jogado["NOME"]} participou: '))
    for c in range(1,pt+1):
        part.append(int(input(f'Quantos gols na {c}° partida: ')))
    t = 0
    for h in part:
        if h != 0:
            t += h
    jogado ['gols'] = part
    jogado ["TOTAL"] = t
    ddo.append(jogado.copy())
    jogado.clear()
    es = str(input('Quer continuar? [S/N]: '))[0]
    while es not in 'nNsS':
        print('ERRO!,Tente novamente apenas S OU N.')
        es = str(input('Quer continuar?[S/N]: '))[0]
    if es in 'nN':
        break
print('\033[;36m-'*12,'\033[;32mTabela de imformaçoes dos jogadores','\033[;36m-'*11)
print()
print(f'\033[;33m{"NO.":<5}{"NOME":<18}{"GOLS":<32}{"TOTAL"}')
print('\033[;36m-'*60,'\033[;31m')
for c in range(0,len(ddo)):
    e = (33-(3*len(ddo[c]["gols"])))
    if e == 1:
        e + 1
    k = ' '*e
    print(f'{c+1:<5}{ddo[c]["NOME"]:<18}{ddo[c]["gols"]}{k}{ddo[c]["TOTAL"]}')
print('\033[;36m-' * 23, '\033[;32mLEVANTAMENTO','\033[;36m-' *23)
while True:
    print('\033[;32m')
    le = int(input('Mostar dados de qual jogaor? '))
    while le > len(ddo) and le != 999:
        print('\033[;31mCodigo invalido! tente novamente.')
        le = int(input('\033[;32mMostar dados de qual jogador? '))
    if le  == 999:
        break
    print('\033[;36m-'*60)
    print(f'--LEVANTAMENTO DO JOGADOR {ddo[le-1]["NOME"]}')
    t = 0
    for c in ddo[le-1]["gols"]:
        t += 1
        print(' '*4,f'\033[;31mNo {t}° jogo ,ele fez {c} gol(s).')
print('\033[;36m-'*20,'\033[;31mPROGRAMA ENCERRADO','\033[;36m-'*20)
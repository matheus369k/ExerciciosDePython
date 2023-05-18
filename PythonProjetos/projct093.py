print('\033[;36m-'*27,'\033[;33mCOLETA DE IMFORMAÇÕES','\033[;36m-'*26)
print('\033[;33m')
jogado = {'NOME':str(input('Nome do Jogador: ')).title()}
part = []
pt = int(input(f'Quantas partidas o jogador {jogado["NOME"]} participou: '))
for c in range(1,pt+1):
    part.append(int(input(f'Quantos gols na {c}° partida: ')))
jogado ['gols'] = part
t = 0
#soma : jogado ["TOTAL"] = sum(part)
for g in part:
    t += g
jogado ['TOTAL'] = t
f = 0
print()
print('\033[;36m-'*28,'\033[;32mREGISTRO DO JOGADOR','\033[;36m-'*27)
print('\033[;32m')
for k,v in jogado.items():
    f +=1
    if f == 1:
        print(f'O {k} do jogador registrado e: {v}.')
    if f == 2:
        print(f'Quantidade de {k} feitos em cada jogo foi: {v}')
print(f'Ao todo o jogador {jogado["NOME"]} fez {jogado["TOTAL"]} gols.')
print()
print('\033[;36m-'*29,'\033[;32mGOLS POR PARTIDA','\033[;36m-'*29)
print('\033[;32m')
print(f'O Jogador {jogado["NOME"]} jogou {len(part)} partidas.')
print()
c = 0
for p in part:
    c += 1
    print(' '*5,f'=>Na partida {c},fez {p} gols.')
print()
print(f'Sendo um total de {jogado["TOTAL"]} gols.')
print()
print('\033[;36m-'*28,'\033[;31mPROGRAMA ENCERRADO','\033[;36m-'*28)


from random import randint
from time import sleep
print('\033[;36m-'*41)
print()
print('\033[;32mGIRANDO DADOS',end='')
for c in range(0,8):
    print('.',end='')
    sleep(0.5)
print('\n')
print('\033[;36m--'*6,'\033[;32mVALORES SORTEADOS','\033[;36m--'*5)
print()
dado = {'jogador1':randint(1,6),'jogador2': randint(1,6),'jogador3':randint(1,6),'jogador4': randint(1,6)  }
for k,v in dado.items():
    print(' '*6,f'\033[;32mO {k} tirou {v} no dado.')
    sleep(1)
print()
print('\033[;36m--'*5,'\033[;32mRank dos jogandores.','\033[;36m-'*11)
h = 6
c = 0
r = 1
print()
#from operator import itemgetter
#ranking {}
#olther: rankng = sorted(dado.items(),key=itemgetter(1),reverse=True)
#Transforma a dict em list
while True:
    for k,v in dado.items():
        c += 1
        if v == h :
            print(' '*6,f'\033[;32m{r}° lugar {k} com {v} pontos.')
            r += 1
        if c == 4:
            c = 0
            h -= 1
    if r == 5:
        break
print()
print('\033[;36m--'*21)



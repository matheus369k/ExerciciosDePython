bra = ('Palmeiras','Flamengo','Cruzeiro','Internacional','Fluminense','Corinthians','Athletico-PR',
       'Atletico','Fortaleza','Sao Paulo','America','Botafogo','Santos','Goias','Red Bull Bragantino',
       'Coritiba','Cuiaba','Gremio','Vasco','Bahia')
alf = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
cont = 5
print('\033[0;36m*TIMES DO BRAZILEIRÃO DE 1° A 20° POSIÇÃO:')
for c in range (0,20):
    print(f'\033[0;31m°{c+1}',bra[c],end='  ')
    if c == cont:
        print('\n',end='')
        cont += 5
print('\n')
print('\033[0;36m*COLOCAÇÃO 5 Primeiros:')
for c in range(0,5):
    print(f'\033[0;31m°{c+1}',bra[c])
print('\n')
print('\033[0;36m*COLOCÃO 4 Ultimos:')
for c in range(1,5):
    print(f'\033[0;31m°{21-c}',bra[-c])
print('\n')
print('\033[0;36m*1° a 20° colocaçao em ordem alfabetica.')
t = y = h  = 0
c = 5
while True:
    if t == 20:
        t = 0
        h += 1
    if bra[t][0] == alf[h]:
        print(f'\033[0;31m°{y+1}',bra[t],end=' ')
        y += 1
    if y == c :
        print('\n',end='')
        c += 5
    t += 1
    if h == 25:
        break
print('\n')
k =bra.index('Sao Paulo')
print(f'\033[36mSAO PAULO ESTA NA °{k+1} Posiçao.')

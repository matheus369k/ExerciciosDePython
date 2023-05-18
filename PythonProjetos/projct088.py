rand = []
ra = []
v = '\033[;31m'
print(f'{v}§§§'*15)
print('  '*5,'\033[;32mJOGA NA MEGA SENA')
print(f'{v}§§§'*15)
from random import randint
from time import sleep
cont = int(input('\033[;32mQuantos jogos voce quer que eu sorteie? '))
print(f'{v}§§§'*15)
c = 0
while True:
    while True:
        num = randint(0,60)
        rand.append(num)
        if rand.count(num) == 2:
            rand.pop()
        if len(rand) == 6:
            break
    ra.append(rand[:])
    rand.clear()
    if c == cont-1:
        break
    c += 1
c = 0
for h in ra:
    c += 1
    h.sort()
    sleep(0.5)
    print(f'\033[;32mJogo {c}: {h}')
print(f'{v}§§§'*15)
print('  '*5,'\033[;32m<  BOA SORTE! >')
print(f'{v}§§§'*15)
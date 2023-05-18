v = '\033[0;32m'
print('\033[0;36m§=§'*15)
n = (int(input('\033[0;33mDigite um numero:' )),
      int(input('Digite outro numero: ')),
      int(input('Digite mais um numero: ')),
      int(input('Digite o ultimo numero: ')))
print('\033[0;36m§=§'*15)
print(f'{v}O numero 9 apareceu {n.count(9)}X.')
j = n.count(3)
if j != 0 :
    print(f'{v}O numero 3 apareceu primeiro na °{n.index(3)+1} posição.')
else:
    print(f'{v}Nao foi digitado o numero 3.')
t = p = 0
for c in range(0,4):
    if n[c]/2%1 == 0:
        if t == 0:
            print(f'{v}Os numeros pares digitados foram',end=' ')
            t += 1
        print(n[c],end=' ')
    elif c == 3 and t == 0:
        if p == 0:
            print(f'{v}Nao foram digitados numeros PARES.',end='')
            p += 1
print('\n',end='')
print('\033[0;36m§=§'*15)


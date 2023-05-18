cont = con = t = 0
num = []
print('\033[;36m§=§'*15)
for c in range(0,9):
    num.append(int(input(f'\033[;33mDigite um valor para[{con}, {cont}]')))
    if cont == 2:
        con += 1
        cont = 0
    else:
        cont += 1
print('\033[;36m§=§'*15)
for c in range(0,9):
    print(f'\033[;31m[{num[c]:^5}]',end=' ')
    t += 1
    if t in (3,6):
        print('\n')
print()
print('\033[;36m§=§'*15)
total = 0
for c in range(0,9):
    if num[c] % 2 == 0:
        total += num[c]
    if c == 0:
        maior = num[3]
    if maior < num[c] and c in (3,4,5):
        maior = num[c]
print(f'A soma dos valores pares e {total}')
soma = num[2] + num[5] + num[8]
print(f'A soma dos valores da terceira coluna e {soma}.')
print(f'O maior valor da segunda linha e {maior}!')
print('\033[;36m§=§'*15)
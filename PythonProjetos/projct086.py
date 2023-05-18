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

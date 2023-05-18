ver = '\033[;32m'
az = '\033[;36m'
print(f'{az}§=§'*20)
list = []
for c in range(0,5):
    list.append(int(input(f'\033[;33mDigite o ®{c+1} valor:')))
print(f'{az}§=§'*20)
print(f'{ver}Os valores digitados foram {list}.')
print(f'{ver}O MAIOR valor digitado foi {max(list)} ele esta na posiçao',end=': ')
for c in range(0,5):
    if max(list) == list[c]:
        print('..',end='')
        print(c+1,end='.')
print(f'\n{ver}O MENOR valor digitado foi {min(list)} ele esta na posiçao',end=': ')
for c in range(0,5):
    if min(list) == list[c]:
        print('..',end='')
        print(c+1,end='.')
print('\n',end='')
print(f'{az}§=§'*20)
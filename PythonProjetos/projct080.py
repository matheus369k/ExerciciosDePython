list = []
v = '\033[;32m'
print('\033[;36m§=§'*15)
for c in range(0,5):
    num = int(input('\033[;33mDigite Um Valor: '))
    if c == 0:
        list.append(num)
        print(f'{v}Adicionado ao final da lista....')
    if num > max(list):
        list.insert(len(list),num)
        print(f'{v}Adicionado ao final da lista....')
    if num < min(list):
        list.insert(0,num)
        print(f'{v}Adicionado ao Inicio da lista...')
    if c >= 2:
        if list[0] < num < list[1]:
            list.insert(1,num)
            print(f'{v}Adicionado a posiçao 1 da lista....')
        if list[1] < num < list[2]:
            list.insert(2,num)
            print(f'{v}Adicionado a posição 2 da lista....')
        if list[2] < num < list[3]:
            list.insert(3,num)
            print(f'{v}Adicionado a posição 3 da lista...')
print('\033[;36m§=§'*15)
print(f'\033[;32mOs valores digitados em ordem foram {list}')
print('\033[;36m§=§'*15)


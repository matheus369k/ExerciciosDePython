list = []
h = c = 0
az = '\033[;36m'
while True:
    print(f'{az}§=§' * 15)
    num = int(input('\033[;33mDigite um valor: '))
    list.append(num)
    h = list.count(num)
    if h > 1:
        print('\033[;31mValor duplicado! Não adicionado ')
        list.remove(num)
    elif h <= 1:
        c += 1
        print(f'\033[;31m{c} N°')
        print('\033[;32mValor adicionado com sucesso!')
    print(f'{az}§=§'*15)
    es = str(input('\033[;33mDeseja continuar: [N/S]')).lower().strip()[0]
    while es not in 'sn':
        es = str(input('\033[;33mDeseja continar: [N/S]')).lower().strip()[0]
    if es == 'n':
        break
print(f'\033[;32mOS numeros digitados foram : {sorted(list)}')
print(f'{az}§=§'*15)


c = 0
list = []
print('\033[;36m§=§'*15)
while True:
    c += 1
    print(F'\033[;31mVALOR {c}')
    list.append(int(input('\033[;33mDigite um valor: ')))
    es = str(input('\033[;33mQuer continuar: [N/S]')).lower().strip()[0]
    while es not in 'ns':
        es = str(input('\033[;33mQuer continuar: [N/S]')).lower().strip()[0]
    print('\033[;36m§=§' * 15)
    if es == 'n':
        break
print(f'\033[;32mVoce digitou {len(list)} elementos.')
list.sort(reverse=True)
print(f'Os valores em ordem decrecente sao {list}.')
if list.count(5) > 0:
    print('\033[;32mO valor 5 faz parte da lista!')
else:
    print('\033[;31mO valor 5 nao faz parte da lista!')
print('\033[;36m§=§'*15)
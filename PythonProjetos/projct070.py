print('\033[0;36m=§='*14)
print('   '*3,'LOJA ULTRA BOM')
print('=§='*14)
vr = '\033[0;32m'
vm = '\033[4;31m'
n = ''
t = m = b = c = 0
while True:
    c += 1
    print('\033[0;36m---'*14)
    nome = str(input('\033[0;33mNome do Produto: '))
    preço = float(input('Preço: R$'))
    cont = str(input('Quer continuar? [S/N]')).lower().strip()[0]
    while cont not in'sn':
        print('\033[0;31mOPÇÃO INVALIDA!!!')
        cont = str(input('\033[0;33mQuer continuar? [S/N]')).lower().strip()[0]
    t += preço
    if preço > 1000:
        m += 1
    if c == 1 or preço < b:
        b = preço
        n = nome
    print(f'\033[0;34m{c}°PRODUTO')
    if cont  == 'n':
        break
print('\033[0;36m$=$'*14)
print(f'\033[0;32mO total das suas comprar foi {vm}{t}R$')
print(f'{m}{vr} Produtos tem o preço acima de {vm}1000R${vr}.')
print(f'O Produto mais barato foi {vm} {n} {vr} custando apenas {vm}{b}R${vr}.')
print('\033[0;36m$=$'*14)
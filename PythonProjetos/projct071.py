az = '\033[0;36m'
print(f'{az}%=%'*11)
print('   '*3,'BANCO H.N')
print('%=%'*11)
sacar = int(input('Valor a ser sacado: R$'))
c = v = d = u = 0
print(f'{az}%=%'*11)
while sacar != 0:
    if sacar >= 50:
        sacar -= 50
        c += 1
    if 20 < sacar < 50:
        sacar -= 20
        v += 1
    if 10 < sacar < 20:
        sacar -= 10
        d += 1
    if  0 < sacar < 10 :
        sacar -= 1
        u += 1
print(f'\033[0;32mTotal de {c} cedulas de R$50.')
print(f'Total de {v} cedulas de R$20.')
print(f'Total de {d} cedulas de R$10.')
print(f'Total de {u} cedulas de R$1.')
print(f'{az}%=%'*11)
print(f'{az}%=% \033[0;35mObrigado pela preferencia {az}%=%')
print(f'%=%=%=%=% \033[0;35mVolte sempre! {az}%7zw=%=%=%=%')

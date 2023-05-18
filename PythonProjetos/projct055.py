print(' '*40,'\033[0;31m< PESO. >')
for c in range(1,6):
    peso = float(input('\033[0;33mDIGITE O PESO DA {}º PESSOA EM( kg ): '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso
print('\033[0;31mO INDIVIDUO MAIS PESADO TEM {}kg.'.format(maior))
print('\033[0;32mO INDIVIDUO MAIS LEVE TEM {}kg.'.format(menor))
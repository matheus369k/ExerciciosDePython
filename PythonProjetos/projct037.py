escolha = int(input('\033[0;35mEscolha o numero inteiro a ser convertido. Digite aqui: '))
print('\033[0;34m- 1 para BINARIO.\n- 2 para OCTAL.\n- 3 para HEXADECIMAL.')
opçao = str(input('\033[0;33mEscolha a base de coversao. Digite aqui: '))

cores = '\033[4;31m'
if opçao == '1':
    print('{} convertido para binario e {}.'.format(escolha,bin(escolha)[2:]))
elif opçao == '3':
    print('{} convertido para HEXADECIMAL e {}.'.format(escolha,hex(escolha)[2:]))
elif opçao == '2':
    print('{} convertido para OCTAL e {}'.format(escolha,oct(escolha)[2:]))
else:
    print('\033[0;31OPÇAO INVALIDA TENTE NOVAMENTE!!!')


print(' '*35,'\033[0;36m< CLASSIFICAÇÃO DE SEXO,IDADE,NOME.... >')
s = 0
maior = 0
mulh = 0
nome0 = ''
for c in range(1,5):
    print('========== {}ºPESSOA =========='.format(c))
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo =  str(input('SEXO FEMININO F/M MASCULINO: ')).lower()
    s += idade
    if maior < idade and sexo == 'm':
        maior = idade
        nome0 = nome
    elif sexo == 'f' and idade < 20:
        mulh = mulh+1
print('==='*15)
print('\033[0;32mA IDADE MEDIA DO GRUPO E DE {}.'.format(s/4))
if maior != 0:
    print('\033[0;34mO HOMEM MAIS VELHO DO GRUPO TEM {} ANOS E SE CHAMA {}.'.format(maior,nome0))
else:
    print('\033[0;31mNAO HA HOMENS NO GRUPO.....')
print('\033[0;34mNO GRUPO HA {} MULHERE(S) COM IDADE ABAIXO DE 20 ANOS.....'.format(mulh))


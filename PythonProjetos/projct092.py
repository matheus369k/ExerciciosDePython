from datetime import datetime
c = 0
while True:
    c += 1
    print('\033[;36m-'*9,f'\033[;32mREGISTO {c}','\033[;36m-'*8)
    print('\033[m')
    dados = {'Nome':str(input('NOME: ')),'A.D.NASCIMENTO':int(input('ANO DE NASCIMENTO: '))}
    atual = datetime.today().year
    idade = atual-dados['A.D.NASCIMENTO']
    del dados['A.D.NASCIMENTO']
    dados ['IDADE'] = idade
    dados ['CTPS'] = int(input('CARTEIRA DE TRABALHO(0 nao tem): N°'))
    if dados['CTPS'] == 0:
        print('\033[;36m-'*4,'\033[;32minformação do Registro','\033[;36m-'*4)
    else:
        dados ['A.D.CONTRATAÇAO'] = int(input('ANO DE CONTRATAÇAO: '))
        dados ['SALARIO'] = float(input('SALARIO: R$'))
        dados ['APOSENTADORIA'] = idade+(35-(atual-dados['A.D.CONTRATAÇAO']))
        print('\033[;36m-'*4,'\033[;32minformação do Registro','\033[;36m-'*4)
    print('\033[m')
    for k,v in dados.items():
        print(f'{k} = {v}')
    print('-' * 30)
    con = str(input('\033[;33mQuer continuar? [S/N]: '))[0]
    while con not in 'sSNn':
        con = str(input('Quer continuar? [S/N]: '))[0]
    if con in 'Nn':
        break
print('\033[;36m-'*30)
print(f'\033[;32m{c} REGISTOS CRIADOS!')
print('\033[;31mPROGAMA ENCERRADO...')

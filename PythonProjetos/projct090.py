g = '\033[;36m'
while True:
    print(f'{g}---'*15)
    aluno = {'\033[;33mNOME':str(input('NOME: ')).title(),
             'MEDIA':float(input('MEDIA: '))}
    print(f'{g}---'*15)
    if aluno["MEDIA"] >= 7:
        aluno ['SITUAÇÃO'] = '\033[;32mAPROVADO!'
    elif 5 < aluno["MEDIA"] < 7 :
        aluno ['SITUAÇÃO'] = '\033[;33mRECUPERAÇÃO!'
    else:
        aluno ['SITUAÇÃO'] = '\033[;31mREPROVADO!'
    for k,v in aluno.items():
        print(f'\033[;33m{k} = {v}')
    print(f'{g}---' * 15)
    aluno.clear()
    es = str(input('\033[;33mQuer continuar: [S/N]'))[0]
    while es not in 'sSnN':
        es = str(input('Quer contimuar: [S/N]'))[0]
    if es in 'nN':
        break
print(f'{g}---'*15)
print('\033[;31mPROGAMA ENCERRADO!')



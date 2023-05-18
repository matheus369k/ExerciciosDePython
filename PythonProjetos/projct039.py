from datetime import date
print('\033[0;35m{ 1 } = HOMEM.\n{ 2 } = MULHER')
sexo = str(input('\033[0;33mQual seu sexo? '))
if '1' == sexo:
    ano = int(input('\033[0;34mDigite aqui seu ano de nascimento: '))
    atual = date.today().year
    idade = atual - ano
    print('Quem nasceu em {} tem {} em {}'.format(ano,idade,atual))
    if idade < 18 :
        print('\033[0;32mAinda falta {} para poder se alistar!!'.format(18-idade))
        print('SEU ANO DE ALISTAMENTO SERA EM {}.'.format(ano+18))
    elif idade == 18:
        print('\033[0;33mVC TEM {} PRECISA SE ALISTAR AGORA!!!'.format(idade))
    else:
        print('O SEU ANO DE ALISTAMENTO FOI EM {}'.format(ano+18))
        print('\033[0;31mVC PASSOU {} DA DATA DE ALISTAMENTO.'.format(idade-18))
elif '2' == sexo:
    print('\033[0;33mO ALISTAMENTO SO E OBRIGATORIO PARA HOMENS.....')
else:
    print('\033[0;31mSO HA DUAS ESCOLHAS')
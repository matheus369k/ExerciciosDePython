print('\033[0;35m$=$'*14)
n_ext = ('Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove',
         'Dez','Onze','Doze','Treze','catorze','Quinze','Dezesseis','Dezessete',
         'Dezoito','Dezenove','Vinte')
while True:
    while True:
        num = int(input('\033[0;33mNumero entre 0 e 20: '))
        if 0 <= num <= 20:
            print(f'\033[0;36mVoce digitou {n_ext[num]}.')
            break
        else:
            print('tente novamente.', end='')
    es = str(input('Deseja continuar:(N PARAR)')).lower().strip()[0]
    if es == 'n':
        break
print('\033[0;35m$=$'*14)

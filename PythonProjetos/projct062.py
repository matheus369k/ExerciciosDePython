ra = int(input('\033[0;33mP1_TERMO: '))
num = int(input('RAZÃO: '))
rein = num*10+ra
qua = s = n = h = 0
while s < rein:
    s += 1
    n = s*num+ra
    print('\033[0;34m{}'.format(n),end=' →')
    if n == rein:
        cont = str(input('\n\033[0;33mQUER CONTIMUIR S/N?')).lower()
        if cont == 's':
            qua = int(input('\033[0;33mQuantidade: '))
            rein += num*qua
        else:
            print('\033[0;32mFORAM MOSTRADOS {} TERMOS.'.format((rein-ra)/num))
            exit()

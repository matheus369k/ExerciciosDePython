list = ('lápis',1.75,37,2,'Borracha',2.00,34,2,'Caderno',15.90,35,1,'Estojo',25.00,36,1,
        'Transferidor',4.20,30,2,'Compasso',9.99,34,2,'Mochila',120.32,35,1,'Canetas',22.30,35,1,
        'Livro',34.90,37,1)
print('\033[0;36m§=§'*18)
print('  '*8,'\033[0;31mLISTAGEM DE PREÇOS')
print('\033[0;36m§=§'*18)
c = g = 0
t = 2
n = 3
h = 1
print('\033[0;31m',end='')
while True:
    g += 1
    print(list[c],end='')
    print('.'*list[t],end='')
    print('R$    ',end='')
    if g != 7:
        print(' '*list[n],end='')
        n += 4
    if g == 6 or g == 7 or g == 1:
        print(list[h])
    else:
        print(list[h],end='')
        print('0')
    h += 4
    c += 4
    t += 4
    if g == 9:
        break
print('\033[0;36m§=§'*18)

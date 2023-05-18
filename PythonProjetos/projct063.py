print('\033[0;34m==='*10)
print('SEQUENCIA FIBONACCI...')
print('==='*10)
ama = '\33[0;33m'
num = int(input('{}TEMOS A SER MOSTRADOS: '.format(ama)))
from time import sleep
h = 0
num -= 1
n = f = 0
k = 5
ver = '\033[4;31m'
clea = '\033[m'
while num != h:
    if h <= 1:
        print(ver,f,ama,end=' → ')
    h += 1
    if h == 1:
        n = f = 1
        print(ver,f,ama,end=' → ')
    if h >= 3:
        n += f
        f = n - f
        print(ver,n,ama,end=' → ')
    if h == k:
        print('\n',end='')
        k += k
print('\033[0;34mFIM.')
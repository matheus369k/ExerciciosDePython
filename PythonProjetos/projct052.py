print(' '*40,'\033[0;34mNUMERO PRIMO.')
num = int(input('\033[0;33mDIGITE O NUMERO AQUI:'))
n = 0
for c in range(1,num+1):
    s = num/c%1
    if s == 0:
        n = n+1
if n == 2 :
    print('\033[0;32mO NUMERO {} E PRIMO.....POR SO TEM {} DIVISORES.'.format(num,n))
else:
    print('\033[0;31mO NUMERO {} NAO E PRIMO.....POR TER {} DIVISORES.'.format(num,n))

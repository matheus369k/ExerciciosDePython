print(' '*40,'\033[0;34m< PALINDROMO >')
frase = str(input('\033[0;33mDIGITE  A PALAVRA OU FRASE A CARGO DE UM POLIGONO: ')).upper()
my1 = frase.split()
m =''.join(my1)
m3 = (len(m)-1)
s = 0
n = 0
t = -1
for c in range(m3,-1,-1):
    t = t + 1
    if m[c] == m[t]:
        s = s+1
    else:
        n = n+1
if s == m3+1 :
    print('\033[0;32mSIM E UMA PALINDROMO.....')
else:
    print('\033[0;31mNÃO E UM PALINDROMO....')
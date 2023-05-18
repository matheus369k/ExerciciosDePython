palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar',
            'mercado','programador','futuro')
vo = ('a','e','i','o','u')
c = t = 0
v = ''
ver = '\033[0;31m'
az = '\033[0;36m'
am = '\033[0;33m'
print('\033[0;32m§=§'*15,end='')
while True:
    cont_c = len(palavras[c][:])
    print(f'\n{ver}( {palavras[c][:].upper()} ){az}Tem as vogais :{am}',end=' ')
    for h in range(0,cont_c):
        t = 0
        if palavras[c][h] == vo[t]:
            print('a',end=' ')
        t += 1
        if palavras[c][h] == vo[t]:
            print('e',end=' ')
        t += 1
        if palavras[c][h] == vo[t]:
            print('i',end=' ')
        t += 1
        if palavras[c][h] == vo[t]:
            print('o',end=' ')
        t += 1
        if palavras[c][h] == vo[t]:
            print('u',end=' ')
    c += 1
    if c == 12:
        break
print('\n',end='')
print('\033[0;32m§=§'*15)
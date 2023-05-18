s = ''
c = 0
while 'F' != s != 'M':
    c += 1
    if c == 1:
        s = str(input('\033[0;33mDIGITE SEU SEXO F/M: ')).upper()
    else:
        s = str(input('\033[0;31mSEXO INVALIDO...POR FAVOR DIGITE SEU SEXO:')).upper()
print('\033[0;32mSEXO {} registadro com sucesso,Obrigado por contribuir.'.format(s))

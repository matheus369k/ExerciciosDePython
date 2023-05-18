print('  '*18,'\033[0;35m<=>'*13)
print('  '*18,'<  CALCULAR O IMC DE UM INDIVIDUL...  >')
print('  '*18,'<->'*13)
peso = float(input('DIGITE AQUI...Peso (Kg):'))
altura = float(input('\033[0;33mDIGITE AQUI...Altura (M):'))
imc = peso/(altura**2)
print('\033[0;34mIMC = {:.1f}'.format(imc))
if imc < 18.5:
    print('\033[0;33mABAIXO Do PESO IDEAL...')
elif 18.5 <= imc < 25:
    print('\033[0;32mPESO IDEAL...')
elif 25 <= imc < 30:
    print('\033[0;33mUM POUCO ACIMA DO PESO IDEAL...')
elif 30 <= imc < 40:
    print('\033[0;31mESTA COM OBESIDADE....')
else:
    print('\033[0;31mESTA COM OBESIDADE MORBIDA....')
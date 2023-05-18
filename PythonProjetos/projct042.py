print(' '*30,'\033[0;34m<->'*20)
print('  '*15,'<   PODE FORMAR UM TRIANGULO E QUAL A SUA CLASSIFICAÇÃO?   >')
print('  '*15,'<->'*20)
a = float(input('\033[0;33mDIGITE AQUI...Lado A:'))
b = float(input('DIGITE AQUI...Lado B:'))
c = float(input('DIGITE AQUI...Lado C:'))
if a  < b+c and b < a+c and c < a+b:
    print('\033[0;32mESSAS RETAS PODE FORMAR UM TRIANGULO!!!')
    if a == b == c:
        print('\033[0;35mTODOS OS LADOS SAO IGUAL PORTANTO E UM TRIANGULO EQUILATERO.....')
    elif a == b or a == c or b == c:
        print('\033[0;35mDOIS LADOS SAO IGUAL, PORTANTO E UM TRIANGULO ISÓSCELES...')
    else:
        print('\033[0;35mTODOS OS  LADOS SAO DIFERENTES PORTANTO E UM TRIANGULO ESCALENO...')
else:
    print('\033[0;31mESSAS RETAS NÃO PODEM FORMAR UM TRIANGULO!!')


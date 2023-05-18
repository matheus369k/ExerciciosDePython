print('  '*20,'\033[0;31m='*23)
print('  '*20,'<  Preço Da Passagem! >')
print('  '*20,'='*23)
km = float(input('\033[7;33;40mquantos km tem sua viagem ao total? '))
if km <= 200:
    total = km*0.50
else:
    total = km*0.45
print('\033[73;32;40mSua viagem de {}km vai custar ao total {}R$!!'.format(km,total))
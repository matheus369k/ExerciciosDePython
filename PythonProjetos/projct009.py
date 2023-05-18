print('\nConverter de metros em:km, hm, deca,deci, cm, mm')
metro = float(input('Digite o valor a ser convertido aqui: '))
deca = metro / 10
hm = deca / 10
km = hm / 10
deci = metro * 10
cm = deci * 10
mm = cm * 10
print('{} metros convertidos em:\n{:.1f} Quilometro(km).\n{:.1f} Hectrometro(hm).\n{:.1f} Decametro(dc).'.format(metro, km, hm, deca))
print('{:.1f} decimetro(dm).\n{:.1f} Centimetro(cm).\n{:.1f} Milimetro(mm).'.format(deci, cm, mm))

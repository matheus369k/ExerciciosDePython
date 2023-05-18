print('\nEscolha o numero a ser mostrado seu dobro, triplo, e raiz.')
numero = float(input('Digite o numero aqui: '))
indice = int(input('Digite o indice da raiz aqui: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero **(1/indice)
print('O numero escolhido foi {}.\nSeu dobro e {}.\nSeu triplo e {}'.format(numero, dobro, triplo))
print('Sua raiz de indice {} e {:.1f}'.format(indice, raiz))

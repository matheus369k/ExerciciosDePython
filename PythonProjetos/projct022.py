nome = str(input('\nDigite seu nome compreto aqui:'))
print('analizando.... seu nome completo {} em maiusculo: '.title().format(nome.upper()))
print('analizando....  seu nome completo {} em Minuscolo: '.title().format(nome.lower()))
nome1 = nome.split()
nome2 =''.join(nome1)
print('Analizando..... Seu nome completo contem {} Letras.'.title().format(len(nome2)))
print('analizando.... seu primeiro nome contem {} letras.'.title().format(len(nome1[0])))










print('\nidentificar uma palavra especifica no inicio de uma frase'.title())
escolha = input('deseja escolha a palavar n/Nao e s/Sim? '.title())
if escolha == 's':
    palavra = input('digite a palavra aqui: '.title())
    n_palavra = len(palavra)
    frase = input('digite a frase aqui: '.title())
    print(palavra in frase[:n_palavra])
if escolha == 'n':
    print('descobrir se a palavra (santo) esta na frase escolhidad'.title())
    frase = input('digite a frase para se analizada aqui: ').title()
    print('Santo' in frase)
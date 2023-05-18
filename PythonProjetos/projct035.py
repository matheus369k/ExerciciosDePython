print('\033[1;35m=--='*8)
print('\033[4;36m<Retas para forma um Triangulo!>')
print('\033[1;35m=--='*8)
ra = float(input('\n\033[0;34mDigite aqui o lado A: '))
rb = float(input('Digite aqui o lado B: '))
rc = float(input('Digite aqui o lado C: '))
if ra < rb+rc and rb < ra+rc and rc < ra+rb :
    print('\033[0;32mESSAS RETAS PODEM FORMAR TRIANGULOS!!!')
else:
    print('\033[0;31mESSA RETAS NAO PODEM FORMAR UM TRIANGULO!!!')
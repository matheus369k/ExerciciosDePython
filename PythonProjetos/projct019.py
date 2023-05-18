from random import shuffle
print('Escolha de alunos em ordem.')
a1 = input('Nome: ')
a2 = input('Nome: ')
a3 = input('Nome: ')
a4 = input('Nome: ')
aleato1 = [a1, a2, a3, a4]
shuffle(aleato1)
print(aleato1)
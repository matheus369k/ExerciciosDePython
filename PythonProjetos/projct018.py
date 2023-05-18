from random import randint, randrange
print('Aluno aleatorio')
n1 = input('1 nome: ')
n2 = input('2 nome: ')
n3 = input('3 nome: ')
n4 = input('4 nome: ')
aluno = randint (1,4)
if aluno == 1 :
    print('aluno selecionado foi {}'.format(n1))
if aluno == 2 :
    print('aluno selecionado foi {}'.format(n2))
if aluno == 3 :
    print('aluno selecionado foi {}'.format(n3))
if aluno == 4 :
    print('aluno selecionado foi {}'.format(n4))
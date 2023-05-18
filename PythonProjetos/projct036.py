#coleta de informaçoẽs
valor_casa = float(input('\033[0;34mValor da Casa:R$'))
salario = float(input('Salario  mensal do individuo:R$'))
anos = int(input('Em quantos anos deseja terminar de pagar o valor da casa: '))
#calculos
prestaçao = valor_casa/(anos*12)
pode_nao = (salario*30)/100
#objetivo
if prestaçao < pode_nao:
    resposta = '\033[4:32mSEU EMPRESTIMO FOI APROVADO!!!'
elif prestaçao > pode_nao:
    resposta = '\033[4:31mSEU EMPRESTIMO FOI NEGADO!!!'
print('\033[0;34mCom as imformaçoẽs obtidas podemos concluir que {}'.format(resposta))

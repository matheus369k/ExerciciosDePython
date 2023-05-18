print('  '*18,'\033[0;35m<->'*9)
print('  '*18,'<  PREÇO DE UM PRODUTO..  >')
print('  '*18,'<->'*9)
preço = float(input('\033[0;33mDIGITE AQUI... O Valor do Produto:R$ '))
print('FORMAS DE PAGAR:\n1 = DINHEIRO OU CHEQUE:A vista 10% de desconto.\n2 = CARTÃO:A vista 5% de desconto.')
print('3 = 2X NO CARTÃO:preço normal.\n4 = 3X OU MAIS NO CARTÃO:20% de juros')
pagamento = str(input('DIGITE AQUIU... A FORMA DE PAGAMENTO: '))
if pagamento == '1':
    valor = preço-(preço*10)/100
    print('\033[0;32mVALOR DO PRODUTO COM 10% DE DESCONTO PASSOU DE {} PARA {} COMO PREÇO FINAL.'.format(preço,valor))
elif pagamento == '2':
    valor = preço-(preço*5)/100
    print('\033[0;32mVALOR DO PRODUTO COM 5% DE DESCONTO PASSOU DE {} PARA {} COMO PREÇO FINAL.'.format(preço,valor))
elif pagamento == '3':
    valor = preço/2
    print('\033[0;32mVALOR  DO PRODUTO 2X NO CARTÃO FICA COM SEU PREÇO NORMAL SENDO ELE {} E DUAS PARCELAS DE {}.'.format(preço,valor))
elif pagamento == '4':
    valor = (preço*20)/100+preço
    X = int(input('EM QUANTAS PARCELAS?'))
    new = valor/X
    print('\033[0;32mVALOR DO PRODUTO {}X NO CARTÃO FICA COM SEU PREÇO 20% ACIMA\n DO NORMAL PASSANDO DE {} PARA {} COM PREÇO FINAL.'.format(X,preço,valor))
    print('E EM {} PARCELAS DE {:.2f}R$.'.format(X,new))
else:
    print('\033[0;31mOPÇÃO INVALIDA DE PAGAMENTO!!!!')

print(' '*30,'\033[0;34m<->'*16)
print(' '*30,'<  MEDIA DE UMA ALUNO, APROVADO OU REPROVADO?  >')
print(' '*30,'<->'*16)
nota1 = float(input('\033[0;36mDIGITE AQUi...Primeira Nota:'))
nota2 = float(input('DIGITE AQUI...Segunda Nota:'))
media = (nota1+nota2)/2
print('\033[0;33mMEDIA {}'.format(media))
if media < 5.0:
    print('\033[0;31mREPROVADO!!!!')
elif 5.0 < media <= 6.9:
    print('\033[0;33mRECUPERAÇÃO!!!!')
else:
    print('\033[0;32mAPROVADO!!!!')

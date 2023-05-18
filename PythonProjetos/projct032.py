from time import sleep
from datetime import date
clea = '\033[m'
print(' '*40,'\033[0;32m>=-='*5+'>')
print(' '*40,'<   Anos Bixestos!  >')
print(' '*40,'>=-='*5+'>',clea)
ano = int(input('\033[7;31mQual o ano a ser analizado digite aqui:',))
print('\033[1;31mANALISANDO.......',clea)
sleep(1)
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0 :
    print('\033[0;30;42mO ANO DE {} E BÍXESTO!!{}'.format(ano,clea))
else:
    print('\033[0;30;41mO ANO DE {} NÃO E BÍXESTO!!!{}'.format(ano,clea))

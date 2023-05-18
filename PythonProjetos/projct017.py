from math import pow, sqrt
print('Trinagulo retangulo.')
cateto_op = float(input('Digite o cateto oposto aqui: '))
cateto_ad = float(input('Digite o cateto adjacente aqui: '))
hipote = sqrt(pow(cateto_ad,2) + pow(cateto_op,2))
print('Analizando....\num triangulo de Cateto Oposto {} e Adjacente {} acaba por ter uma Hipotenuza igual a {:.2f}.'.format(cateto_op,cateto_ad,hipote))


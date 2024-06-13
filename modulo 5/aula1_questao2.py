import random
import math

qtde=int(input('Digite quantos números aleatórios entre 0 e 100 você deseja: \n'))
cont=0

for i in range(0, qtde, 1):
    num=random.randint(1, 100)
    cont+=num

raiz=math.sqrt(cont)

print('O valor da raiz quadrada dos números aleatórios é: {}'.format(raiz))

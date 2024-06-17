import random

n=random.randint(1, 10)

while True: 
    palpite = int(input('Tente acertar! Digite um número aleatório entre 1 e 10: \n'))

    if palpite > n: 
        print('Esse número é mais alto que o aleatório! Tente novamente!')
    elif palpite < n: 
        print('Esse número é mais baixo do que o aleatório! Tente novamente!')
    elif palpite == n:
        break

print("Correto! O número é: {}".format(n))

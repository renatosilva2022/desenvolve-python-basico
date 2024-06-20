import random

num_elementos = random.randint(5, 20)

elementos = [random.randint(1, 10) for _ in range(num_elementos)]

print("Lista de elementos:", elementos)

soma_elementos = sum(elementos)
print("Soma dos elementos:", soma_elementos)

media_elementos = soma_elementos / num_elementos
print("Média dos elementos:", media_elementos)

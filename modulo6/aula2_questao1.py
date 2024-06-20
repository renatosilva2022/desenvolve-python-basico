import random

original = [random.randint(-100, 100) for _ in range(20)]

ordenada = sorted(original)

print("Lista ordenada:")
print(ordenada)

print("\nLista original:")
print(original)

maior = original.index(max(original))
print("\nÍndice do maior valor:", maior)

menor = original.index(min(original))
print("Índice do menor valor:", menor)

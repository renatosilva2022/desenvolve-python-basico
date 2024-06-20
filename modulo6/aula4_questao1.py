pares = [x for x in range(20, 51) if x % 2 == 0]

quadrados = [x ** 2 for x in range(1, 10)]

divisiveis_por_7 = [x for x in range(1, 101) if x % 7 == 0]

paridade = ["par" if x % 2 == 0 else "impar" for x in range(0, 30, 3)]

print("Números pares entre 20 e 50:", pares)
print("Quadrados dos números de 1 a 9:", quadrados)
print("Números divisíveis por 7 entre 1 e 100:", divisiveis_por_7)
print("Paridade para valores de 0 a 27 de 3 em 3:", paridade)

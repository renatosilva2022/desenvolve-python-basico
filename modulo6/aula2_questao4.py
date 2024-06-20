def receber_lista(n):
    return [int(input(f"Digite o {i+1}º elemento: ")) for i in range(n)]

n1 = int(input("Digite a quantidade de elementos da lista 1: "))
l1 = receber_lista(n1)

n2 = int(input("Digite a quantidade de elementos da lista 2: "))
l2 = receber_lista(n2)

l_intercalada = []
min_length = min(len(l1), len(l2))

for i in range(min_length):
    l_intercalada.append(l1[i])
    l_intercalada.append(l2[i])

l_intercalada.extend(l1[min_length:])
l_intercalada.extend(l2[min_length:])

print("Lista intercalada:", ' '.join(map(str, l_intercalada)))

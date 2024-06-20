import random
from collections import Counter

l1 = [random.randint(0, 50) for _ in range(20)]
l2 = [random.randint(0, 50) for _ in range(20)]

intersecao = list(set(l1).intersection(l2))

cont_l1 = Counter(l1)
cont_l2 = Counter(l2)

print("lista1 -", l1)
print("lista2 -", l2)
print("Intersecao -", sorted(intersecao))

print("cont")
for elemento in sorted(intersecao):
    print(f"{elemento}: (l1={cont_l1[elemento]}, l2={cont_l2[elemento]})")

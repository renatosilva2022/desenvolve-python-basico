import random

lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

max_count = 0
current_count = 0
start_index = 0

for i in range(len(lista)):
    if lista[i] < 0:
        if current_count == 0:
            temp_start = i
        current_count += 1
    else:
        if current_count > max_count:
            max_count = current_count
            start_index = temp_start
        current_count = 0

if current_count > max_count:
    max_count = current_count
    start_index = temp_start

del lista[start_index:start_index + max_count]

print("Editada: ", lista)

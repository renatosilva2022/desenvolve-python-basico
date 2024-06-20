num = []
print("Digite pelo menos 4 números inteiros. Digite 'sair' para finalizar a entrada.")

while len(num) < 4 or entrada != 'sair':
    entrada = input("Digite um número ou 'sair': ")
    if entrada.isdigit():
        num.append(int(entrada))
    elif entrada == 'sair' and len(num) >= 4:
        break
    elif entrada != 'sair':
        print("Por favor, digite um número inteiro ou 'sair'.")

print("Lista original:", num)

print("Três primeiros elementos:", num[:3])

print("Dois últimos elementos:", num[-2:])

print("Lista invertida:", num[::-1])

print("Elementos de índice par:", num[::2])

print("Elementos de índice ímpar:", num[1::2])

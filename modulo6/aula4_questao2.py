frase = input("Digite uma frase: ")

vogais = 'aeiouAEIOU'
consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

l_vogais = sorted([char for char in frase if char in vogais])
l_consoantes = [char for char in frase if char in consoantes]

print("Vogais:", l_vogais)
print("Consoantes:", l_consoantes)
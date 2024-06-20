frase = input("Digite uma frase: ").lower() 

vogais = 'aeiou'
indices_vogais = []
contagem_vogais = 0

for indice, caracter in enumerate(frase):
    if caracter in vogais:
        indices_vogais.append(indice)
        contagem_vogais += 1

print(f"{contagem_vogais} vogais")
print("Índices", indices_vogais)
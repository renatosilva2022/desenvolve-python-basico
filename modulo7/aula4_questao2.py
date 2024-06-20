import re

with open("frase.txt", "r") as arquivo:
    conteudo = arquivo.read()

conteudo_limpo = re.sub(r'[^\w\s]', '', conteudo)

palavras = conteudo_limpo.split()
conteudo_final = '\n'.join(palavras)

with open("palavras.txt", "w") as novo_arquivo:
    novo_arquivo.write(conteudo_final)

print("Conteúdo de 'palavras.txt':")
with open("palavras.txt", "r") as arquivo_lido:
    print(arquivo_lido.read())

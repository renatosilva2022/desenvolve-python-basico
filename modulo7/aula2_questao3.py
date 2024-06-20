import re

def verificar_palindromo():
    while True:
        frase = input("Digite uma frase (digite 'fim' para encerrar): ")
        if frase.lower() == "fim":
            break
        else:
            
            frase_limpa = re.sub(r'[\W_]', '', frase.lower())
            
            if frase_limpa == frase_limpa[::-1]:
                print(f'"{frase}" é palíndromo')
            else:
                print(f'"{frase}" não é palíndromo')

verificar_palindromo()

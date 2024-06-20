import random

def carregar_palavra():
    with open("gabarito_forca.txt", "r") as arquivo:
        palavras = arquivo.readlines()
    return random.choice(palavras).strip()

def carregar_enforcado():
    with open("gabarito_enforcado.txt", "r") as arquivo:
        return arquivo.readlines()

def imprime_forca(palavra, letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()

def imprime_enforcado(erros):
    enforcado = carregar_enforcado()
    print('\n'.join(enforcado[:erros]))

def jogar_forca():
    palavra = carregar_palavra()
    letras_corretas = set()
    letras_erradas = set()
    tentativas_restantes = 6

    print("Bem-vindo ao jogo da forca!")
    print("A palavra tem {} letras.".format(len(palavra)))

    while tentativas_restantes > 0:
        imprime_forca(palavra, letras_corretas)
        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
        elif letra in palavra:
            letras_corretas.add(letra)
            if len(letras_corretas) == len(set(palavra)):
                print("Parabéns! Você acertou a palavra:", palavra)
                break
        else:
            letras_erradas.add(letra)
            tentativas_restantes -= 1
            print("Letra errada! Você tem mais {} tentativas.".format(tentativas_restantes))
            imprime_enforcado(6 - tentativas_restantes)

    else:
        print("Você foi enforcado! A palavra era:", palavra)

jogar_forca()

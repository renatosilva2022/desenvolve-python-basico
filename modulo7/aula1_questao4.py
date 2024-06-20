def formatar_numero_celular(numero):
    
    if len(numero) == 8:
        numero = '9' + numero

    numero_formatado = numero[:5] + '-' + numero[5:]

    return numero_formatado

numero_celular = input("Digite o número do celular: ")

numero_completo = formatar_numero_celular(numero_celular)
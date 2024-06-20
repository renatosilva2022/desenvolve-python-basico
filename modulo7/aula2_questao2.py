def substituir_vogais():
   
    frase = input("Digite uma frase: ")
        
    vogais = "aeiouAEIOU"
    traducao = str.maketrans(vogais, '*' * len(vogais))
    
    frase_modificada = frase.translate(traducao)
    
    print("Frase modificada:", frase_modificada)

substituir_vogais()

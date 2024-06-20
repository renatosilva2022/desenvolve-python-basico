import random

def encrypt(nomes):
    
    chave_aleatoria = random.randint(1, 10)
 
    nomes_cript = []
    
    for nome in nomes:
        nome_cript = ""
        for char in nome:
          
            novo_char_code = ord(char) + chave_aleatoria
                        
            if novo_char_code > 126:
                novo_char_code = 33 + (novo_char_code - 127)
                        
            nome_cript += chr(novo_char_code)
        
        nomes_cript.append(nome_cript)
    
    return nomes_cript, chave_aleatoria

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

nomes_criptografados, chave = encrypt(nomes)

print("Chave aleatória:", chave)
print("Nomes criptografados:", nomes_criptografados)

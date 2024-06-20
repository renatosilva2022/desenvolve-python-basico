def find_anagrams(text, target):
    
    text = text.lower()
    target = target.lower()
    target_sorted = ''.join(sorted(target))
    
    words = text.split()
    anagrams = []
  
    for word in words:
        if ''.join(sorted(word)) == target_sorted:
            anagrams.append(word)
    
    return anagrams

frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

anagramas_encontrados = find_anagrams(frase, palavra_objetivo)

print("Anagramas:", anagramas_encontrados)
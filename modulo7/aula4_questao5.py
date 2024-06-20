# Dados dos livros
livros = [
    {"Título": "Dom Quixote", "Autor": "Miguel de Cervantes", "Ano de publicação": 1605, "Número de páginas": 863},
    {"Título": "1984", "Autor": "George Orwell", "Ano de publicação": 1949, "Número de páginas": 328},
    {"Título": "Cem Anos de Solidão", "Autor": "Gabriel García Márquez", "Ano de publicação": 1967, "Número de páginas": 417},
    {"Título": "O Pequeno Príncipe", "Autor": "Antoine de Saint-Exupéry", "Ano de publicação": 1943, "Número de páginas": 93},
    {"Título": "Orgulho e Preconceito", "Autor": "Jane Austen", "Ano de publicação": 1813, "Número de páginas": 279},
    {"Título": "Harry Potter e a Pedra Filosofal", "Autor": "J.K. Rowling", "Ano de publicação": 1997, "Número de páginas": 223},
    {"Título": "A Metamorfose", "Autor": "Franz Kafka", "Ano de publicação": 1915, "Número de páginas": 201},
    {"Título": "O Senhor dos Anéis", "Autor": "J.R.R. Tolkien", "Ano de publicação": 1954, "Número de páginas": 1178},
    {"Título": "Crime e Castigo", "Autor": "Fiódor Dostoiévski", "Ano de publicação": 1866, "Número de páginas": 551},
    {"Título": "O Alquimista", "Autor": "Paulo Coelho", "Ano de publicação": 1988, "Número de páginas": 163}
]

# Abrir o arquivo CSV para escrita
with open("meus_livros.csv", "w") as arquivo:
    # Escrever o cabeçalho
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")

    # Escrever os dados dos livros
    for livro in livros:
        arquivo.write("{},{},{},{}\n".format(
            livro["Título"],
            livro["Autor"],
            livro["Ano de publicação"],
            livro["Número de páginas"]
        ))

print("Arquivo 'meus_livros.csv' criado com sucesso!")

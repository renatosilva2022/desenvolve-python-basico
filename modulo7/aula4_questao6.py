import csv

def processar_arquivo_spotify(filename):
   
    musicas_populares = []

    musicas_por_ano = {}

    with open(filename, 'r', encoding='latin-1') as file:
       
        leitor_csv = csv.reader(file)

        next(leitor_csv)

        for linha in leitor_csv:
            
            if '"' in linha[0] or '"' in linha[1]:
                continue

            track_name = linha[0]
            artist_name = linha[1]
            released_year = int(linha[3])
            streams = int(linha[8])

            if 2012 <= released_year <= 2022:
           
                if released_year not in musicas_por_ano or streams > musicas_por_ano[released_year][3]:
                    musicas_por_ano[released_year] = [track_name, artist_name, released_year, streams]

    for ano, musica in musicas_por_ano.items():
        musicas_populares.append(musica)

    return musicas_populares

spotify_file = "spotify-2023.csv"
musicas_populares = processar_arquivo_spotify(spotify_file)

print("Lista de músicas mais populares por ano:")
for musica in musicas_populares:
    print(musica)

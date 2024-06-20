import re

with open("estomago.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print("Primeiras 25 linhas:")
for line in lines[:25]:
    print(line.strip())

total_lines = len(lines)
print("\nNúmero total de linhas:", total_lines)

longest_line = max(lines, key=len)
print("\nLinha com maior número de caracteres:", longest_line.strip())
print("Número de caracteres:", len(longest_line.strip()))

pattern_nonato = re.compile(r"\bNonato\b", re.IGNORECASE)
pattern_iria = re.compile(r"\bÍria\b", re.IGNORECASE)
count_nonato = sum(len(pattern_nonato.findall(line)) for line in lines)
count_iria = sum(len(pattern_iria.findall(line)) for line in lines)

print("\nNúmero de menções a Nonato:", count_nonato)
print("Número de menções a Íria:", count_iria)

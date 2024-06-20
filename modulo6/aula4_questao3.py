horas_trab = [40, 37, 45, 40, 40, 48]
ganho_por_hora = 20
hora_extra = 25

pag = [
    ganho_por_hora * min(hora, 40) + hora_extra * max(0, hora - 40)
    for hora in horas_trab
]

print(pag)

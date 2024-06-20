def valida_cpf(cpf):
  
    cpf = cpf.replace('.', '').replace('-', '')
    if len(cpf) != 11 or not cpf.isdigit():
        return "Inválido"
    
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        primeiro_digito = 0
    else:
        primeiro_digito = 11 - resto
    
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        segundo_digito = 0
    else:
        segundo_digito = 11 - resto
    
    if primeiro_digito == int(cpf[9]) and segundo_digito == int(cpf[10]):
        return "Válido"
    else:
        return "Inválido"

cpf_usuario = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")
resultado = valida_cpf(cpf_usuario)
print(resultado)

#5) Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) e escreva uma expressão que imprima True se a pessoa já pode se aposentar, ou False caso contrário, de acordo com as seguintes regras:

gênero= (input("Gênero M ou F? "))
idade=int(input("Idade em anos: "))
Tserviço=int(input("Tempo de serviço em anos: "))
#A: Para mulheres, ter mais de 60 anos. Para homens, 65.
a = (gênero == 'F' and idade >= 60) or \
    (gênero == 'M' and idade >= 65) 
#B: Ou ter trabalhado pelo menos 30 anos
b = Tserviço>30 
#C: Ou ter 60 anos  e trabalhado pelo menos 25.
c = idade>= 60 and Tserviço >= 25
podeaposentar= a or b or c
print(podeaposentar)
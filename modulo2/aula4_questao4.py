#4) Escreva um programa que leia um valor inteiro referente a uma quantia em reais e
#calcule a menor quantidade possível de notas necessárias para pagar aquele valor.
#As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída deve estar formatada exatamente como indicado. 
#Entrada:
#576
#Saída:
#5 nota(s) de R$100,00
#1 nota(s) de R$50,00
#1 nota(s) de R$20,00
#0 nota(s) de R$10,00
#1 nota(s) de R$5,00
#0 nota(s) de R$2,00
#1 nota(s) de R$1,00

#Entrada
quant=int(input("Digite um valor inteiro referente a uma quantia em reais"))
#Processamento
notas100= quant //100  
quant= quant % 100

notas50= quant //50  
quant= quant % 50

notas20= quant //20 
quant= quant % 20

notas10= quant //10
quant= quant % 10

notas5= quant //5 
quant= quant % 5

notas2= quant //2 
quant= quant % 2

notas1= quant //1 
quant= quant % 1

#Saída
print((f"{notas100} de R$100,00"))
print((f"{notas50} de R$50,00"))
print((f"{notas20} de R$20,00"))
print((f"{notas10} de R$10,00"))
print((f"{notas5} de R$5,00"))
print((f"{notas2} de R$2,00"))
print((f"{notas1} de R$1,00"))
#The first line of input contains an integer N indicating the number of test cases that follows.
# Each test case contains an integer Amount (1 ≤ Amount ≤ 15) which represents the amount of animal used and a character Type ('C', 'R' or 'S'),
#Print the total of animals used, the total of each type of animal and the percentual of each one in relation of the total of animals used. The percentual must be printed with 2 digits after the decimal point.

n=int(input("Quantos experimentos foram feitos?: "))
cont=0
quant=0
c=0#coelho
r=0 #rato
s=0 #sapo

while n != cont:
    tipo=input("coelho,rato ou sapo?: ")
    quant=int(input("Quantos animais foram utilizados?: "))
    
    cont =cont+1
    if tipo=="coelho":
        c=c+quant
    elif tipo=="rato":
        r=r+quant
    elif tipo=="sapo":
        s=s+quant
    else:
        print("Tipo inválido, tente novamente!")
        cont=cont-1
totalcobaias=s+c+r
print("Total de animais utilizados: ", s+r+c)
print(f"Foram utilizados {c} coelhos, {r} ratos e {s} sapos")
print(f"Sapos representam {s/totalcobaias*100:2.2f}%, coelhos representam {c/totalcobaias*100:2.2f}% e ratos representam {r/totalcobaias*100:2.2f}%")
        
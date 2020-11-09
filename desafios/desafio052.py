numero = int(input("Digite um numero inteiro: "))

cont = 0

for c in range(1, numero):
    if(numero % c == 0 and numero % numero == 0):
        cont = cont + 1

if(cont == 1):
    print("O numero {0} e PRIMO!".format(numero))
else:
    print("O numero {0} NAO E PRIMO!".format(numero))

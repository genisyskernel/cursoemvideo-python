num1 = float(input("Informe o primeiro numero: "))
num2 = float(input("Informe o segundo numero: "))

if(num1 > num2):
    maior = num1
    print("O primeiro valor {0} e MAIOR!".format(num1))
elif(num2 > num1):
    maior = num2
    print("O segundo valor {0} e MAIOR!".format(num2))
else:
    print("Nao existe valor MAIOR! Os dois sao IGUAIS!")

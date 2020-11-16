numero = float(input("Digite um numero: "))

total = 1

while numero != 0:
    print("{0}x".format(numero), end="")
    total *= numero
    numero = numero - 1

if(numero == 0):
    print(" > {0}".format(total), end="")



numero = float(input("Digite um numero para calcular seu Fatorial: "))

total = 1

print("Calculando o Fatorial !{} = ".format(numero), end="")

while numero != 0:
    print("{0}".format(numero), end="")
    print(" x " if numero > 1 else " = ", end="")
    total *= numero
    numero -= 1

#for c in range(0, int(numero)):
#    print("{0}".format(numero), end="")
#    print(" x " if numero > 1 else " = ", end="")
#    total *= numero
#    numero -= 1

print("{0}".format(total), end="")

# from math import factorial
# n = int(input("Digite um numero: "))
# f = factorial(n)
# print("O fatorial de {0} e {1}.".format(n, f))

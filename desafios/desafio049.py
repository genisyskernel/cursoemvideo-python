numero = int(input("Digite um numero para ver sua tabuada: "))

for c in range(1, 11):
    tabuada = numero * c
    print("{0} x {1:2} = {2:2}".format(numero, c, tabuada))

numero = int(input("Digite um numero inteiro: "))

for c in range(0, 11):
    tabuada = numero * c
    print("{0} x {1:2} = {2:2}".format(numero, c, tabuada))

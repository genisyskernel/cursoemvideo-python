soma = 0
for c in range(1, 7):
    numero = int(input("Digite o {0} valor: ".format(c)))
    if(numero % 2 == 0):
        soma += numero
print("A soma dos numeros pares vale: {0}.".format(soma))

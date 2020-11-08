soma = 0
for c in range(0, 6):
    numero = int(input("Digite um numero inteiro: "))
    if(numero % 2 == 0):
        soma += numero
print("A soma dos numeros pares vale: {0}.".format(soma))

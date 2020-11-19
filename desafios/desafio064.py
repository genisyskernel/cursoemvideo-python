numero = 0
soma = 0
cont = 0

while(numero != 999):
    numero = int(input("Digite um numero inteiro: "))

    if(numero != 999):
        cont += 1
        soma += numero

print("Foram digitados {0} numeros! Desconsiderando o FLAG ( 999 ).".format(cont))
print("A soma de todos os numeros informados foi {0}! Desconsiderando o FLAG ( 999 ).".format(soma))

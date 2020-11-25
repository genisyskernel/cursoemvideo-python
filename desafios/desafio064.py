numero = soma = cont = 0

numero = int(input("Digite um numero inteiro [ 999 para sair ]: "))

while(numero != 999):
    cont += 1
    soma += numero
    numero = int(input("Digite um numero inteiro [ 999 para sair ]: "))

print("Foram digitados {0} numeros! Desconsiderando o FLAG ( 999 ).".format(cont))
print("A soma de todos os numeros informados foi {0}!".format(soma))

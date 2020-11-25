sair = False
soma = 0
media = 0
cont = 0
maior = 0
menor = 0

while(sair == False):

    numero = int(input("Informe um numero inteiro: "))

    cont += 1

    soma += numero

    opcao = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]

    if(opcao == "S"):
        sair = False
    elif(opcao == "N"):
        sair = True
        media = soma / cont

    if(cont == 1):
        maior = numero
        menor = numero
    elif(numero > maior):
        maior = numero
    elif(numero < menor):
        menor = numero

print("O MAIOR numero: {0} | O MENOR numero: {1}.".format(maior, menor))
print("A media entre os {0} valores vale: {1:.2f}!".format(cont, media))

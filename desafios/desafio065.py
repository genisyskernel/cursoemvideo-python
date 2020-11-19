sair = False
soma = 0
media = 0
cont = 0
maior = 0
menor = 0
numero_anterior = 0
numero_atual = 0

while(sair == False):

    numero = int(input("Informe um numero inteiro: "))

    numero_atual = numero

    cont += 1

    soma += numero

    opcao = str(input("Deseja continuar? [S/N]: ")).strip().upper()

    if(opcao == "S"):
        sair = False
    elif(opcao == "N"):
        sair = True
        media = soma / cont

    if(numero_atual > numero_anterior):
        maior = numero_atual
    else:
        maior = numero_anterior

    if(numero_atual < numero_anterior):
        menor = numero_atual
    else:
        menor = numero_anterior

    numero_anterior = numero_atual

print("O MAIOR numero: {0} | O MENOR numero: {1}.".format(maior, menor))

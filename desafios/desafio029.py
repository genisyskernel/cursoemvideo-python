velocidade = float(input("Digite a velocidade em que o carro esta (KM/H): "))

if velocidade > 80:
    print("Voce ultrapassou 80 KM/H e foi multado!\n")
    valor_multa = (velocidade - 80) * 7
    print("Valor da multa a pagar R$: {0:.2f} reais.\n".format(valor_multa))
    print("Mais cuidado com a velocidade!")
else:
    print("Cuidado com a velocidade na estrada!")

print("Boa viagem!")

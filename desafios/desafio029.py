velocidade = float(input("Digite a velocidade em que o carro esta (KM/H): "))
limite = 80
if velocidade > limite:
    print("Voce ultrapassou o limite de {0} KM/H e foi multado!".format(limite))
    print("-.-"*20)
    valor_multa = (velocidade - limite) * 7
    print("Valor da multa a pagar R$: {0:.2f} reais.".format(valor_multa))
    print("Mais cuidado com a velocidade!")
else:
    print("Cuidado com a velocidade na estrada!")

print("-.-"*20)
print("Boa viagem!")

distancia = float(input("Informa a distancia da viagem em KM/H: "))

if distancia <= 200:
    preco_passagem = distancia * 0.50
else:
    preco_passagem = distancia * 0.45

# Opcao do `if` simplificado;
# preco_passagem = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print("-*-"*20)
print("Sua viagem de {0} KM/H vai custar R$: {1:.2f} reais.".format(distancia, preco_passagem))
print("-*-"*20)

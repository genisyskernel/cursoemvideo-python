distancia = float(input("Informa a distancia da viagem em KM/H: "))

if distancia <= 200:
    preco_passagem = 0.50 * distancia
else:
    preco_passagem = 0.45 * distancia

print("Sua viagem de {0} KM/H vai custar R$: {1:.2f} reais.".format(distancia, preco_passagem))

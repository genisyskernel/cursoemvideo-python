distancia = float(input("\033[1;34mInforma a distancia da viagem em KM/H: \033[m"))

if distancia <= 200:
    preco_passagem = distancia * 0.50
else:
    preco_passagem = distancia * 0.45

# Opcao do `if` simplificado;
# preco_passagem = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print("\033[7;30m-*-\033[m"*20)
print("\033[1;32mSua viagem de\033[m \033[1;31m{0} KM/H\033[m \033[1;32mvai custar\033[m \033[1;31mR$: {1:.2f} "
      "reais\033[m\033[1;32m.\033[m".format(distancia, preco_passagem))
print("\033[7;30m-*-\033[m"*20)

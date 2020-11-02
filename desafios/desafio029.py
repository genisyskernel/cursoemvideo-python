velocidade = float(input("\033[1;36mDigite a velocidade em que o carro esta (KM/H): \033[m"))
limite = 80
if velocidade > limite:
    print("\033[1;31mVoce ultrapassou o limite de\033[m \033[1;30m{0}\033[m \033[1;31mKM/H e foi multado!\033[m".format(limite))
    print("\033[7;30m-.-\033[m"*20)
    valor_multa = (velocidade - limite) * 7
    print("\033[1;31mValor da multa a pagar\033[m \033[1;32mR$: {0:.2f} reais\033[m\033[1;31m.\033[m".format(valor_multa))
    print("\033[1;31mMais cuidado com a velocidade!\033[m")
else:
    print("\033[1;33mCuidado com a velocidade na estrada!\033[m")

print("\033[7;30m-.-\033[m"*20)
print("\033[1;32mBoa viagem!\033[m")

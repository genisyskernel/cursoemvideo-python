preco = float(input("\033[1;36mDigite o preco do produto?\033[m \033[0;32mR$\033[m"))

novo_preco = preco - (preco * 5 / 100) # 5% de R$ 10 reais : (10*5/100)

print("\033[1;31mPreco normal\033[m \033[1;32mR$: {0:.2f}\033[m\n\033[1;31mPreco com\033[m \033[1;30m5%\033[m \033[1;31mde desconto\033[m \033[1;32mR$: {1:.2f}\033[m".format(preco, novo_preco))

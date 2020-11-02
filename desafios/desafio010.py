valor_real = float(input("\033[1;30mDigite o valor na carteira?\033[m \033[1;32mR$\033[m"))

dolares = valor_real / 3.27

print("\033[1;37mO valor\033[m \033[1;32mR$: {0:.2f} reais\033[m \033[1;37mpode comprar\033[m \033[1;32mUSD$: {1:.2f} dolares\033[m \033[1;37m!\033[m".format(valor_real, dolares))

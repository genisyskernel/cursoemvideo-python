numero = int(input("\033[1;31mDigite um numero de 0 a 9999: \033[m"))

print("\033[1;30mAnalisando o numero\033[m \033[1;37m{0}\033[m".format(numero))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print("""\033[1;32mUnidade:\033[m \033[1;37m{0}\033[m
\033[1;34mDezena:\033[m \033[1;37m{1}\033[m
\033[1;35mCentena:\033[m \033[1;37m{2}\033[m
\033[1;36mMilhar:\033[m \033[1;37m{3}\033[m""".format(unidade, dezena, centena, milhar))

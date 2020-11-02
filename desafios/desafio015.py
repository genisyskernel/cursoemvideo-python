qtd_km = float(input("\033[1;30mInforme a quantidade de KM rodados:\033[m "))
qtd_dias_alugado = float(input("\033[1;30mQuantos dias alugados?\033[m "))

valor_km = 0.15
valor_dia = 60

custo = (qtd_km * valor_km) + (qtd_dias_alugado * valor_dia)

print("\033[1;37mValor a pagar\033[m \033[4;32mR$ {0:.2f} reais.\033[m".format(custo))

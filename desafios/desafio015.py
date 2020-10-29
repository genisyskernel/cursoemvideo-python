qtd_km = float(input("Informe a quantidade de KM rodados: "))
qtd_dias_alugado = float(input("Quantos dias alugados? "))

valor_km = 0.15
valor_dia = 60

custo = (qtd_km * valor_km) + (qtd_dias_alugado * valor_dia)

print("Valor a pagar R$ {0:.2f} reais.".format(custo))

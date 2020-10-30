numero = int(input("Digite um numero de 0 a 9999: "))

print("Analisando o numero {0}".format(numero))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print("""Unidade: {0}
Dezena: {1}
Centena: {2}
Milhar: {3}""".format(unidade, dezena, centena, milhar))

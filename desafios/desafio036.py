valor_casa = float(input("Informe o valor da casa: R$ "))

salario_comprador = float(input("Informe o seu salario mensal: R$ "))

qtd_ano = int(input("Em quantos anos voce deseja pagar a casa? "))

limite_pagamento = salario_comprador*30/100

valor_prestacao = valor_casa / (qtd_ano * 12)

print()
print("Valor da casa: R$ {0:.2f} reais.".format(valor_casa))
print("Voce vai ficar {0} anos pagando a parcela.".format(qtd_ano))
print("Valor da parcela mensal: R$ {0:.2f} reais.".format(valor_prestacao))

if valor_prestacao >= limite_pagamento:
    print("Infelizmente voce nao pode FINANCIAR ESSA CASA!")
else:
    print("Verificado que voce se QUALIFICA para a compra da CASA! Parabens!")

salario = float(input("Salario do funcionario: "))

novo_salario = salario + (salario*15/100)

print("Salario normal R$: {0:.2f} reais\nSalario com 15% de aumento R$: {1:.2f} reais".format(salario, novo_salario))

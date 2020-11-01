salario = float(input("Informe o salario R$: "))

if salario > 1250:
    aumento = 10
else:
    aumento = 15

salario_novo = salario + salario*aumento/100

print("Salario antigo R$: {0:.2f} reais.".format(salario))
print("Salario com {0}% de aumento. R$ {1:.2f} reais.".format(aumento, salario_novo))

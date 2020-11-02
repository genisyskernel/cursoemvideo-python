salario = float(input("\033[1;32mInforme o salario R$: \033[m"))

if salario > 1250:
    aumento = 10
else:
    aumento = 15

salario_novo = salario + salario*aumento/100

print("\033[1;31mSalario antigo\033[m \033[1;32mR$: {0:.2f} reais\033[m\033[1;31m.\033[m".format(salario))
print("\033[1;31mSalario com\033[m \033[1;30m{0}%\033[m \033[1;31mde aumento.\033[m \033[1;32mR$ {1:.2f} reais\033["
      "m\033[1;31m.\033[m".format(aumento, salario_novo))

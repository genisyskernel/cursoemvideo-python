salario = float(input("\033[4;36mSalario do funcionario: \033[m"))

novo_salario = salario + (salario*15/100)

print("\033[4;36mSalario normal\033[m \033[4;32mR$: {0:.2f} reais\033[m\n\033[4;36mSalario com\033[m \033[4;30m15%\033[m \033[4;36mde aumento\033[m \033[4;32mR$: {1:.2f} reais\033[m".format(salario, novo_salario))

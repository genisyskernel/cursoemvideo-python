from random import shuffle

aluno01 = str(input("\033[1;33mDigite o nome do primeiro aluno(a): \033[m"))
aluno02 = str(input("\033[1;33mDigite o nome do segundo aluno(a): \033[m"))
aluno03 = str(input("\033[1;33mDigite o nome do terceiro aluno(a): \033[m"))
aluno04 = str(input("\033[1;mDigite o nome do quarto aluno(a): \033[m"))

ordem_apresentacao = [aluno01, aluno02, aluno03, aluno04]
shuffle(ordem_apresentacao)

print("\033[1;37mA apresentação vai ser na ordem:\033[m \n\033[1;30m {0}\033[m\033[1;37m!.\033[m".format(ordem_apresentacao))

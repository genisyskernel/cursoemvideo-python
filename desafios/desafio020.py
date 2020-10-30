from random import shuffle

aluno01 = str(input("Digite o nome do primeiro aluno(a): "))
aluno02 = str(input("Digite o nome do segundo aluno(a): "))
aluno03 = str(input("Digite o nome do terceiro aluno(a): "))
aluno04 = str(input("Digite o nome do quarto aluno(a): "))

ordem_apresentacao = [aluno01, aluno02, aluno03, aluno04]
shuffle(ordem_apresentacao)

print("A apresentação vai ser na ordem: \n {0}.".format(ordem_apresentacao))

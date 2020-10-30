from random import choice

aluno01 = str(input("Digite o nome do aluno(a) 01: "))
aluno02 = str(input("Digite o nome do aluno(a) 02: "))
aluno03 = str(input("Digite o nome do aluno(a) 03: "))
aluno04 = str(input("Digite o nome do aluno(a) 04: "))

aluno_aleatorio = choice([aluno01, aluno02, aluno03, aluno04])

print("O aluno(a) {0} foi escolhido(a) para apagar o quadro!".format(aluno_aleatorio))

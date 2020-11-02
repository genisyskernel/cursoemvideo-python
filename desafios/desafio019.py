from random import choice

aluno01 = str(input("\033[1;32mDigite o nome do aluno(a) 01: \033[m"))
aluno02 = str(input("\033[1;32mDigite o nome do aluno(a) 02: \033[m"))
aluno03 = str(input("\033[1;32mDigite o nome do aluno(a) 03: \033[m"))
aluno04 = str(input("\033[1;32mDigite o nome do aluno(a) 04: \033[m"))

aluno_aleatorio = choice([aluno01, aluno02, aluno03, aluno04])

print("\033[1;36mO aluno(a)\033[m \033[1;30m{0}\033[m \033[1;36mfoi escolhido(a) para apagar o quadro!\033[m".format(aluno_aleatorio))

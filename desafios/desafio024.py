nome_cidade = str(input("\033[1;31mDigite o nome da sua cidade: \033[m"))

divide_nome = nome_cidade.upper().strip().split()

verificar_nome = "SANTO" in divide_nome[0]
print("\033[1;32mTem escrito SANTO no nome da cidade?\033[m {0}{1}{2}".format("\033[1;30m", verificar_nome, "\033[m"))

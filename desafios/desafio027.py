nome_completo = str(input("\033[1;30mDigite seu nome completo: \033[m"))

dividir_nome = nome_completo.strip().split()
print("\033[1;31mSeu primeiro nome e:\033[m \033[1;32m{0}\033[m\033[1;31m.\033[m".format(dividir_nome[0]))
print("\033[1;31mSeu ultimo nome e:\033[m \033[1;32m{0}\033[m\033[1;31m.\033[m".format(dividir_nome[len(dividir_nome) - 1]))

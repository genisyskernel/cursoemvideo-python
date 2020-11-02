nome_completo = str(input("\033[7;30mDigite seu nome completo: \033[m")).strip()

print("\033[1;34mSeu nome em MAIUSCULO:\033[m \033[1;33m{0}\033[m\033[1;34m.\033[m".format(nome_completo.upper()))
print("\033[1;34mSeu nome em MINUSCULO:\033[m \033[1;33m{0}\033[m\033[1;34m.\033[m".format(nome_completo.lower()))
print("\033[1;34mSeu nome tem\033[m \033[1;33m{0}\033[m \033[1;34mletras sem os espacos.\033[m".format(len(nome_completo.strip().replace(" ", ""))))
#print("Seu nome tem {0} letras sem os espacos.".format(len(nome_completo) - nome_completo.count(" ")))
primeiro_nome = nome_completo.split()
#print("Seu primeiro nome: {0} e tem {1} letras.".format(primeiro_nome[0], nome_completo.find(" ")))
print("\033[1;34mSeu primeiro nome:\033[m \033[1;33m{0}\033[m \033[1;34me tem \033[m\033[1;33m{1}\033[m \033[1;34mletras.\033[m".format(primeiro_nome[0], len(primeiro_nome[0])))

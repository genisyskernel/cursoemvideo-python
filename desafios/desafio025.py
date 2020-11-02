nome_completo = str(input("\033[1;33mDigite o seu nome completo: \033[m"))

print("\033[1;30mSeu nome tem Silva?\033[m \033[1;36m{0}\033[m".format("SILVA" in nome_completo.strip().upper()))

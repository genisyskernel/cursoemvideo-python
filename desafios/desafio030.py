numero_inteiro = int(input("\033[1;35mDigite um numero inteiro: \033[m"))

if numero_inteiro % 2 == 0:
    print("\033[1;36mO numero\033[m \033[1;35m{0}\033[m \033[1;36me\033[m \033[1;35mPAR\033[m\033[1;36m!\033[m".format(numero_inteiro))
else:
    print("\033[1;36mO numero\033[m \033[1;35m{0}\033[m \033[1;36me\033[m \033[1;35mIMPAR\033[m\033[1;36m!\033[m".format(numero_inteiro))

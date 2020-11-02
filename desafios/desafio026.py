frase = str(input("\033[4;31mDigite uma frase qualquer: \033[m")).strip().upper()

print("\033[4;36mA letra\033[m \033[4;34mA\033[m \033[4;36maparece\033[m \033[4;34m{0}\033[m \033[1;36mna frase.\033[m".format(frase.count("A")))
print("\033[4;36mA primeira lentra\033[m \033[4;34mA\033[m \033[4;36maparece na posicao\033[m \033[4;34m{0}.\033[m".format(frase.find("A") + 1))
print("\033[4;36mA ultima lentra\033[m \033[1;34mA \033[4;36maparece na posicao\033[m \033[4;34m{0}.\033[m".format(frase.rfind("A") + 1))

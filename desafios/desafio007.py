nota01 = float(input("\033[4;30mDigite a primeira nota: \033[m"))
nota02 = float(input("\033[4;20mDigite a segunda nota: \033[m"))

media = (nota01 + nota02) / 2

print("Media das notas \033[1;31m{0:.1f}\033[m e \033[1;32m{1:.1f}\033[m e igual: \033[1;34m{2:.1f}\033[m".format(nota01, nota02, media))

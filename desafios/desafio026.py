frase = str(input("Digite uma frase qualquer: ")).strip().upper()

print("A letra A aparece {0} na frase.".format(frase.count("A")))
print("A primeira lentra A aparece na posicao {0}.".format(frase.find("A") + 1))
print("A ultima lentra A aparece na posicao {0}.".format(frase.rfind("A") + 1))

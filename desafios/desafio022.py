nome_completo = str(input("Digite seu nome completo: "))

print("Seu nome em MAIUSCULO: {0}.".format(nome_completo.upper()))
print("Seu nome em MINUSCULO: {0}.".format(nome_completo.lower()))
print("Seu nome tem {0} letras sem os espacos.".format(len(nome_completo.strip().replace(" ", ""))))
#print("Seu nome tem {0} letras sem os espacos.".format(len(nome_completo) - nome_completo.count(" ")))
primeiro_nome = nome_completo.split()
#print("Seu primeiro nome: {0} e tem {1} letras.".format(primeiro_nome[0], nome_completo.find(" ")))
print("Seu primeiro nome: {0} e tem {1} letras.".format(primeiro_nome[0], len(primeiro_nome[0])))

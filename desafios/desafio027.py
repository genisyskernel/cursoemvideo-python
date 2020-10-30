nome_completo = str(input("Digite seu nome completo: "))

dividir_nome = nome_completo.strip().split()
print("Seu primeiro nome e: {0}.".format(dividir_nome[0]))
print("Seu ultimo nome e: {0}.".format(dividir_nome[len(dividir_nome) - 1]))

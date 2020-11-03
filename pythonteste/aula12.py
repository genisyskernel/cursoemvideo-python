nome = str(input("Qual e o seu nome: "))
if nome == "Eduardo":
    print("Que nome bonito!")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("Seu nome e bem popular no Brasil!")
elif nome in "Ana Claudia Jessica Juliana":
    print("Belo nome feminino!")
else:
    print("Seu nome e bem normal!")
print("Tenho um bom dia, {0}!".format(nome))

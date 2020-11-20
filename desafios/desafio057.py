sexo = str(input("Informe seu sexo [ M / F]: ")).strip().upper()[0]

while sexo != "M" and sexo != "F":

    print("Dados invalidos! ", end="")
    sexo = str(input("Por favor informe seu sexo [ M / F ]: "))

if(sexo == "M"):
    print("Seu sexo e {0}!".format("MASCULINO"))
else:
    print("Seu sexo e {0}!".format("FEMININO"))
print("Sexo registrado com sucesso!")

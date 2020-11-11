sexo = ""

while sexo != "M" and sexo != "F":
    sexo = str(input("Informe seu sexo [ M / F]: ")).upper()

if(sexo == "M"):
    print("Seu sexo e {0}!".format("MASCULINO"))
else:
    print("Seu sexo e {0}!".format("FEMININO"))

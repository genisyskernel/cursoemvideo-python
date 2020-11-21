termo = int(input("Informe o primeiro termo: "))

razao = int(input("Informe a razao: "))

tot = termo
cont = 1
termo_final = 1

while termo_final != 0:

    #print("Cont: {0}".format(cont))
    #print("Termo final: {0}".format(termo_final))

    if(cont >= termo_final ):
        termo_final = int(input("Ate quanto mais termo voce deseja ir? "))
        cont = 0
    else:
        cont += 1
        print("{0} -> ".format(tot), end="")
        tot += razao

print("ACABOU")

termo = int(input("Informe o primeiro termo: "))

razao = int(input("Informe a razao: "))

tot = termo
cont = 1
termo_final = 11
termos_mostrados = 0

while termo_final != 0:

    #print("Cont: {0}".format(cont))
    #print("Termo final: {0}".format(termo_final))

    if(cont >= termo_final ):
        print("PAUSA", end="")
        termo_final = int(input("\nAte quanto mais termo voce deseja ir? "))
        cont = 0
    else:
        termos_mostrados += 1
        cont += 1
        print("{0} -> ".format(tot), end="")
        tot += razao

print("Progressao finalizada com {0} termos mostrados.".format(termos_mostrados))
print("ACABOU")

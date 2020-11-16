termo = int(input("Informe o primeiro termo: "))

razao = int(input("Informe a razao: "))


tot = 1
cont = 0
termo_final = 1

while termo_final != 0:
    if(termo_final == cont):
        termo_final = int(input("Ate quanto mais termo voce deseja ir? "))

    print("{0} -> ".format(tot), end="")
    cont += 1
    tot += (termo + razao) - 1

print("ACABOU")

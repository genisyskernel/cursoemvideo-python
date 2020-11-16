termo = int(input("Informe o primeiro termo: "))

razao = int(input("Informe a razao: "))

tot = 1
cont = 0

while cont != 10:
    print("{0} -> ".format(tot), end="")
    cont += 1
    tot += (termo + razao) - 1

print("ACABOU")

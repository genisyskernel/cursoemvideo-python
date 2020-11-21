termo = int(input("Informe o primeiro termo: "))

razao = int(input("Informe a razao: "))

tot = termo
cont = 0

while cont != 10:
    print("{0} -> ".format(tot), end="")
    cont += 1
    tot += razao

print("ACABOU")

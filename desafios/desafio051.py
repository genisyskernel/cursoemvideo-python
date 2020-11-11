primeiro_termo = int(input("Informe o primeiro termo: "))

razao = int(input("Informe a razao da P.A: "))

decimo = primeiro_termo + (10 - 1) * razao

cont = 0
for c in range(primeiro_termo, decimo + razao, razao):
    if(cont < 10):
        cont += 1
        print(c, end=" -> ")
print("ACABOU")

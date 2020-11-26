n = cont = 0
while True:
    n = int(input("Informe um numero para ver sua tabuada: "))
    cont = 0

    if n < 0:
        break

    print("-" * 15)
    while cont <= 10:
        tabuada = n * cont
        print(f"{n:2} x {cont:2} = {tabuada:3}")
        cont += 1
    print("-"*15)
print("SAINDO DO PROGRAMA DE TABUADA! Volte sempre...")

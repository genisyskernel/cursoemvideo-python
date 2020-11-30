while True:
    n = int(input("Informe um numero para ver sua tabuada: "))

    if n < 0:
        break

    print("-" * 15)
    for c in range(1, 11):
        tabuada = n * c
        print(f"{n:2} x {c:2} = {tabuada:3}")
    print("-"*15)
print("SAINDO DO PROGRAMA DE TABUADA! Volte sempre...")

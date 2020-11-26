n = s = cont = 0
while n != 999:
    n = int(input("Digite um numero inteiro ( 999 para parar ): "))

    if n == 999:
        break

    s += n
    cont += 1
print(f"A soma de {cont} valores vale {s}!")

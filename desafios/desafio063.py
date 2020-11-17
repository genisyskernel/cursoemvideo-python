numero = int(input("Informe um numero inteiro: "))

cont = 1
fibonacci = 0
termo_anterior = 0

while cont < numero:
    print("{0}".format(fibonacci), end=" -> ")

    termo_anterior = cont - 1
    fibonacci = cont + termo_anterior
    cont += 1

print("FIM")

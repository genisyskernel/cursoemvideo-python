Fn = int(input("Informe um numero inteiro: "))

cont = 0
cont_1 = 0
cont_2 = 1
fibonacci = 0

while cont < Fn:

    print("{0}".format(fibonacci), end=" -> ")

    fibonacci = cont_1 + cont_2

    cont_1 += cont_2

    cont_2 = cont_1 - cont_2

    # controle
    cont += 1

print("FIM")

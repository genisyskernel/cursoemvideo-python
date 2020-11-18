Fn = int(input("Informe um numero inteiro: "))

cont = 0
fibonacci = 0
termo_anterior = 0
termo_posterior = 0

while cont < Fn:

    termo_anterior += cont

    cont += 1

    termo_posterior += cont

    fibonacci = termo_posterior - termo_anterior

    print("{0}".format(fibonacci), end=" -> ")

print("FIM")

numero = int(input("Digite um numero inteiro: "))

cont = 0

for c in range(1, numero + 1):
    if(numero % c == 0):
        cont += 1
        print("\033[1;32m", end="")
    else:
        print("\033[1;31m", end="")
    print("{0}".format(c), end=" ")
    print("\033[m", end="")

print("\nO numero {0} foi divisivel {1} vezes, ".format(numero, cont), end="")
if(cont == 2):
    print("e por isso ele E PRIMO!")
else:
    print("e por isso ele NAO E PRIMO!")

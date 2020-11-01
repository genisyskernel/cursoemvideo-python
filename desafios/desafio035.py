r1 = float(input("Digite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("As retas A: {0} | B: {1} | C: {2} FORMAM um triangulo!".format(r1, r2, r3))
else:
    print("As retas A: {0} | B: {1} | C: {2} NAO FORMAM um triangulo!".format(r1, r2, r3))

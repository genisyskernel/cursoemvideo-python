r1 = float(input("\033[1;37mDigite o comprimento da primeira reta: \033[m"))
r2 = float(input("\033[1;36mDigite o comprimento da segunda reta: \033[m"))
r3 = float(input("\033[1;35mDigite o comprimento da terceira reta: \033[m"))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("\033[1;30mAs retas\033[m \033[1;37mA: {0}\033[m \033[1;30m|\033[m \033[1;36mB: {1}\033[m \033[1;30m|\033[m "
          "\033[1;35mC: {2}\033[m \033[1;32mFORMAM um triangulo\033[m\033[1;30m!\033[m".format(r1, r2, r3))

    if (r2 == r1 == r3):
        tipo = "EQUILATERO"
    elif (r2 != r1 != r3):
        tipo = "ESCALENO"
    else:
        tipo = "ISOSCELES"

    print("O triangulo e um {0}!".format(tipo))

else:
    print("\033[1;30mAs retas\033[m \033[1;37mA: {0}\033[m \033[1;30m|\033[m \033[1;36mB: {1}\033[m \033[1;30m|\033[m "
          "\033[1;35mC: {2}\033[m \033[1;31mNAO FORMAM um triangulo\033[m\033[1;30m!\033[m".format(r1, r2, r3))

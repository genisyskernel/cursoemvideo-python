numero01 = float(input("Informe o primeiro numero: "))
numero02 = float(input("Informe o segundo numero: "))
numero03 = float(input("Informe o terceiro numero: "))

if numero01 > numero02 and numero01 > numero03:
    print("O numero {0} e o MAIOR!".format(numero01))
elif numero02 > numero01 and numero02 > numero03:
    print("O numero {0} e o MAIOR!".format(numero02))
elif numero03 > numero01 and numero03 > numero02:
    print("O numero {0} e o MAIOR!".format(numero03))

if numero01 < numero02 and numero01 < numero03:
    print("O numero {0} e o MENOR!".format(numero01))
elif numero02 < numero01 and numero02 < numero03:
    print("O numero {0} e o MENOR!".format(numero02))
elif numero03 < numero02 and numero03 < numero01:
    print("O numero {0} e o MENOR!".format(numero03))

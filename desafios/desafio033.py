numero01 = float(input("Informe o primeiro numero: "))
numero02 = float(input("Informe o segundo numero: "))
numero03 = float(input("Informe o terceiro numero: "))

"""
if numero01 > numero02 and numero01 > numero03:
    maior = numero01
elif numero02 > numero01 and numero02 > numero03:
    maior = numero02
elif numero03 > numero01 and numero03 > numero02:
    maior = numero03

if numero01 < numero02 and numero01 < numero03:
    menor = numero01
elif numero02 < numero01 and numero02 < numero03:
    menor = numero02
elif numero03 < numero02 and numero03 < numero01:
    menor = numero03
"""

menor = numero01
if numero02 < numero01 and numero02 < numero03:
    menor = numero02
if numero03 < numero01 and numero03 < numero02:
    menor = numero03

maior = numero01
if numero02 > numero01 and numero02 > numero03:
    maior = numero02
if numero03 > numero01 and numero03 > numero02:
    maior = numero03

print("O numero {0} e o MENOR!".format(menor))
print("O numero {0} e o MAIOR!".format(maior))

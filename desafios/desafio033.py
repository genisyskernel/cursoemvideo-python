numero01 = float(input("\033[1;33mInforme o primeiro numero: \033[m"))
numero02 = float(input("\033[1;34mInforme o segundo numero: \033[m"))
numero03 = float(input("\033[1;35mInforme o terceiro numero: \033[m"))

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

print("\033[1;30mO numero\033[m \033[1;37m{0}\033[m \033[1;30me o\033[m \033[1;31mMENOR\033[m\033[1;30m!\033[m".format(menor))
print("\033[1;30mO numero\033[m \033[1;37m{0}\033[m \033[1;30me o\033[m \033[1;34mMAIOR\033[m\033[1;30m!\033[m".format(maior))

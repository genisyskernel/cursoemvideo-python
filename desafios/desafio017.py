from math import hypot

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)
hipotenusa_na_mao = ((cateto_oposto * cateto_oposto) + (cateto_adjacente * cateto_adjacente)) ** (1/2)

print("A hipotenusa do cateto oposto {0} e do cateto adjacente {1} vale {2:.2f}.".format(cateto_oposto, cateto_adjacente, hipotenusa))

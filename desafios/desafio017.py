from math import hypot

cateto_oposto = float(input("\033[7;30mDigite o comprimento do cateto oposto:\033[m "))
cateto_adjacente = float(input("\033[7;30mDigite o comprimento do cateto adjacente:\033[m "))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)
hipotenusa_na_mao = ((cateto_oposto * cateto_oposto) + (cateto_adjacente * cateto_adjacente)) ** (1/2)

print("\033[7;30mA hipotenusa do cateto oposto\033[m \033[7;37m{0}\033[m \033[7;30me do cateto adjacente\033[m \033[7;37m{1}\033[m \033[7;30mvale\033[m \033[7;37m{2:.2f}.\033[m".format(cateto_oposto, cateto_adjacente, hipotenusa))

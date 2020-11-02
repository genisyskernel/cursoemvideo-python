from math import sin, cos, tan, radians

angulo = float(input("\033[1;35mDigite um angulo qualquer:\033[m "))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("\033[1;32mO angulo\033[m \033[1;31m{0}\033[m \033[1;32mtem o seno\033[m \033[3;31m{1:.2f}\033[m\033[1;32m, cosseno\033[m \033[1;31m{2:.2f}\033[m \033[1;32me a tangente\033[m \033[1;31m{3:.2f}\033[m\033[1;32m.\033[m".format(angulo, seno, cosseno, tangente))

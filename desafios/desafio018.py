from math import sin, cos, tan, radians

angulo = float(input("Digite um angulo qualquer: "))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("O angulo {0} tem o seno {1:.2f}, cosseno {2:.2f} e a tangente {3:.2f}.".format(angulo, seno, cosseno, tangente))

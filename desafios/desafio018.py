from math import sin, cos, tan

angulo = float(input("Digite um angulo qualquer: "))

seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)

print("O angulo {0} tem o seno {1:.2f}, cosseno {2:.2f} e a tangente {3:.2f}.".format(angulo, seno, cosseno, tangente))

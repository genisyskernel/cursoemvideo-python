from random import randint
from time import sleep

print("\033[7;30m-=-\033[m"*20)
numero_usuario = int(input("\033[1;34mInforme um numero inteiro de 0 a 5: \033[m"))

numero_sorteado = randint(0, 5)

print("\033[4;30mVerificando se o seu numero foi o escolhido...\033[m")
print("\033[7;30m-=-\033[m"*20)

sleep(3)

if numero_usuario == numero_sorteado:
    print("\033[1;32mParabens! Voce advinhou o numero sorteado, que foi\033[m \033[1;37m{0}\033[m\033[1;37m!\033[m".format(numero_sorteado))
else:
    print("\033[1;31mVoce errou! O numero sorteado foi\033[m \033[1;37m{0}\033[m\033[1;37m!\033[m".format(numero_sorteado))
print("\033[7;30m-=-\033[m"*20)

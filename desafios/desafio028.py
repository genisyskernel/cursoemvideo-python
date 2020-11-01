from random import randint
from time import sleep

print("-=-"*20)
numero_usuario = int(input("Informe um numero inteiro de 0 a 5: "))

numero_sorteado = randint(0, 5)

print("Verificando se o seu numero foi o escolhido...")
print("-=-"*20)

sleep(3)

if numero_usuario == numero_sorteado:
    print("Parabens! Voce advinhou o numero sorteado, que foi {0}!".format(numero_sorteado))
else:
    print("Voce errou! O numero sorteado foi {0}!".format(numero_sorteado))
print("-=-"*20)

from random import randint
from time import sleep

vitorias = 0

while True:

    jogador_escolha = " "
    while jogador_escolha not in "PI":
        jogador_escolha = str(input("[JOGADOR]: Voce escolhe PAR ou IMPAR [ P/I ]? ")).strip().upper()[0]
    computador_numero = randint(0, 5)
    print("[COMPUTADOR]: Pensei em um numero...")
    jogador_numero = int(input("[JOGADOR]: Informe um numero ( 0 ate 5 ): "))

    if jogador_escolha == "P":
        computador_escolha = "I"
    else:
        computador_escolha = "P"

    if jogador_numero <= 10 and jogador_numero >= 0:
        print("PAR.. ")
        sleep(2)
        print("OU..")
        sleep(2)
        print("IMPAR!!!")
        sleep(1)
        total = jogador_numero + computador_numero
        verificar = total % 2
        if verificar == 0:
            vitoria = "PAR"
        else:
            vitoria = "IMPAR"

        print("*=" * 40)
        print(f"[GAME]: Voce jogou {jogador_numero} e o computador {computador_numero}. Total vale {total} e deu {vitoria}!")
        print("*=" * 40)

        if computador_escolha == vitoria[0]:
            print(f"[COMPUTADOR]: Eu ganhei! Numero: {computador_numero} | Vitoria: {vitoria}")
            print("-="*40)
            break
        else:
            print(f"[JOGADOR]: Voce ganhou! Parabens! Numero: {jogador_numero} | Vitoria: {vitoria}")
            vitorias += 1
            print("-="*40)
    else:
        print("[JOGADOR]: Erro! Informe um numero de 0 ate 5! Tente novamente!")
print(f"GAME OVER! Voce ganhou {vitorias} vezes!")

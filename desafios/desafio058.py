from random import randint

computador = randint(0, 10)

jogador = 0
cont_tentativas = 0
acertou = False


while acertou == False:
    jogador = int(input("Tente advinhar o numero sorteado de 0 a 10: "))
    cont_tentativas += 1
    if(jogador == computador):
        acertou = True
        print("\033[1;32mParabens! Voce acertou o numero sorteado, que foi {0}!\033[m".format(computador))
        print("\033[1;34mVoce tentou {0} vezes para acertar o numero!\033[m".format(cont_tentativas))
    elif(jogador < computador):
        print("\033[1;31mMAIS! Quase acertou! Tente novamente...\033[m")
    elif(jogador > computador):
        print("\033[1;31mMENOS! Quase acertou! Tente novamente...\033[m")

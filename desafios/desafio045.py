from random import randint

jogador = int(input("1 = PAPEL"
                    "\n2 = TESOURA"
                    "\n3 = PEDRA"
                    "\nQual voce vai escolher? "))

nome = str(input("Qual o seu nick no jogo? "))

computador = randint(1, 3)

# 1 = PAPEL
# 2 = TESOURA
# 3 = PEDRA

ganhador = "COMPUTADOR"
jogador_escolha = "PAPEL"
computador_escolha = "PAPEL"

# COMPUTADOR = TESOURA
if(jogador == 1 and computador == 2):
    jogador_escolha = "PAPEL"
    computador_escolha = "TESOURA"
    ganhador = "COMPUTADOR"
elif(jogador == 3 and computador == 2):
    jogador_escolha = "PEDRA"
    computador_escolha = "TESOURA"
    ganhador = nome

# COMPUTADOR = PEDRA
elif(jogador == 2 and computador == 3):
    jogador_escolha = "TESOURA"
    computador_escolha = "PEDRA"
    ganhador = "COMPUTADOR"
elif(jogador == 1 and computador == 3):
    jogador_escolha = "PAPEL"
    computador_escolha = "PEDRA"
    ganhador = nome

# COMPUTADOR = PAPEL
elif(jogador == 3 and computador == 1):
    jogador_escolha = "PEDRA"
    computador_escolha = "PAPEL"
    ganhador = "COMPUTADOR"
elif(jogador == 2 and computador == 1):
    jogador_escolha = "TESOURA"
    computador_escolha = "PAPEL"
    ganhador = nome

# JOGADOR = PAPEL
elif(jogador == 1 and computador == 3):
    jogador_escolha = "PAPEL"
    computador_escolha = "PEDRA"
    ganhador = nome
elif(jogador == 1 and computador == 2):
    jogador_escolha = "PAPEL"
    computador_escolha = "TESOURA"
    ganhador = "COMPUTADOR"

# JOGADOR = TESOURA
elif (jogador == 2 and computador == 1):
    jogador_escolha = "TESOURA"
    computador_escolha = "PAPEL"
    ganhador = nome
elif (jogador == 2 and computador == 3):
    jogador_escolha = "TESOURA"
    computador_escolha = "PEDRA"
    ganhador = "COMPUTADOR"

# JOGADOR = PEDRA
elif(jogador == 3 and computador == 1):
    jogador_escolha = "PAPEL"
    computador_escolha = "PEDRA"
    ganhador = nome
elif(jogador == 3 and computador == 2):
    jogador_escolha = "PEDRA"
    computador_escolha = "TESOURA"
    ganhador = nome

# EMPATE #
elif(jogador == 1 == computador):
    ganhador = "EMPATE"
    jogador_escolha = "PAPEL"
    computador_escolha = "PAPEL"
elif(jogador == 2 == computador):
    ganhador = "EMPATE"
    jogador_escolha = "TESOURA"
    computador_escolha = "TESOURA"
elif(jogador == 3 == computador):
    ganhador = "EMPATE"
    jogador_escolha = "PEDRA"
    computador_escolha = "PEDRA"
else:
    print("\033[1;31mOpcao invalida! Tente novamente!\033[m")
    ganhador = "NINGUEM"
    jogador_escolha = "ERRO"
    computador_escolha = "ERRO"

#print(computador)
print("\033[1;32m|{0}|\033[m = \033[1;31m[ {1} ]\033[m <+[=====] \033[1;30mVS\033[m [=====]+> \033[1;32m|{2}|\033[m = \033[1;31m[ {3} ]\033[m".format("COMPUTADOR", computador_escolha, nome, jogador_escolha))
print("O \033[1;34mGANHADOR\033[m FOI O \033[1;36m{0}\033[m!".format(ganhador))

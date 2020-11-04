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
if(jogador == 3 and computador == 2):
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
    ganhador = nome

print(computador)
print("|{0}| = [ {1} ] <+[=====] vs [=====]+> |{2}| = [ {3} ]".format("COMPUTADOR", computador_escolha, nome, jogador_escolha))
print("O GANHADOR FOI O {0}!".format(ganhador))

from datetime import date

ano_atual = date.today().year
cont_maior = 0
cont_menor = 0

for c in range(1, 8):
    ano_nascimento = int(input("Digite o ano de nascimento da {0} pessoa: ".format(c)))

    idade = ano_atual - ano_nascimento

    if(idade >= 21):
        cont_maior += 1
    else:
        cont_menor += 1

print("A quantidade de pessoas que sao MAIORES de idade sao {0}!".format(cont_maior))
print("E as que sao MENORES de idade sao {0}!".format(cont_menor))

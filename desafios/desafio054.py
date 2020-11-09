from datetime import date

ano_atual = date.today().year
cont_maior = 0
cont_menor = 0

for c in range(0, 7):
    ano_nascimento = int(input("Digite o ano de nascimento: "))

    if(ano_atual - ano_nascimento >= 21):
        cont_maior += 1
    else:
        cont_menor += 1

print("A quantidade de pessoas que sao MAIORES de idade sao {0}!".format(cont_maior))
print("A quantidade de pessoas que sao MENORES de idade sao {0}!".format(cont_menor))

from datetime import date

ano_nascimento = int(input("Informe seu ano de nascimento: "))

ano_atual = date.today().year

idade = ano_atual - ano_nascimento

if(idade <= 9):
    categoria = "MIRIM"
elif(idade <= 14):
    categoria = "INFANTIL"
elif(idade <= 19):
    categoria = "JUNIOR"
elif(idade <= 20):
    categoria = "SENIOR"
else:
    categoria = "MASTER"

print("Ano de nascimento: {0}.\nIdade: {1} anos.\nCategoria: {2}.".format(ano_nascimento, idade, categoria))

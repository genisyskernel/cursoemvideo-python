from datetime import date

ano_nascimento = int(input("Informe seu ano de nascimento: "))

sexo = str(input("Informe seu sexo (M, F): "))

ano_atual = date.today().year

idade = ano_atual - ano_nascimento

idade_alistamento = 18

print("Quem nasceu no ano de {0} tem {1} anos em {2}.".format(ano_nascimento, idade, ano_atual))

if(sexo == "M" and idade < idade_alistamento):
    tempo_alistamento = idade_alistamento - idade
    print("Voce ainda precisa se alistar ao servico MILITAR! Falta {0} anos.".format(tempo_alistamento))
    print("Seu alistamento vai ser em {0}!".format(ano_atual + tempo_alistamento))
elif(sexo == "M" and idade == idade_alistamento):
    print("Voce tem que se alistar IMEDIATAMENTE!")
elif(sexo == "M" and idade > idade_alistamento):
    tempo_alistamento = idade - idade_alistamento
    print("Voce passou do tempo para se alistar! Passou {0} anos.".format(tempo_alistamento))
    print("Seu alistamento foi em {0}!".format(ano_atual - tempo_alistamento))
else:
    print("Voce e do sexo FEMININO e nao precisa fazer o alistamento obrigatorio!")
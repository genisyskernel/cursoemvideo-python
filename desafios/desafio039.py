from datetime import date

ano_nascimento = int(input("Informe seu ano de nascimento: "))

ano_atual = date.today().year

idade = ano_atual - ano_nascimento

idade_alistamento = 18

if(idade < idade_alistamento):
    tempo_alistamento = idade_alistamento - idade
    print("Voce ainda precisa se alistar ao servico MILITAR! Falta {0} anos.".format(tempo_alistamento))
elif(idade == idade_alistamento):
    print("Voce esta na hora de se alistar! Ano atual {0}.".format(ano_atual))
elif(idade > idade_alistamento):
    tempo_alistamento = idade - idade_alistamento
    print("Voce passou do tempo para se alistar! Passou {0} anos.".format(tempo_alistamento))

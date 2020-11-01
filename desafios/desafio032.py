from datetime import date

ano = int(input("Informe qualquer ano (Digite 0 para informar o ano atual): "))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {0} E BISSEXTO!".format(ano))
else:
    print("O ano {0} NAO E BISSEXTO!".format(ano))

ano = int(input("Informe qualquer ano: "))

if ano % 4 == 0 or ano % 400 == 0 or ano % 100 != 0:
    print("O ano {0} E BISSEXTO!".format(ano))
else:
    print("O ano {0} NAO E BISSEXTO!".format(ano))

from datetime import date

ano = int(input("\033[1;30mInforme qualquer ano\033[m \033[1;37m(Digite 0 para informar o ano atual):\033[m "))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("\033[1;30mO ano\033[m \033[1;37m{0}\033[m \033[1;32mE BISSEXTO!\033[m".format(ano))
else:
    print("\033[1;30mO ano\033[m \033[1;37m{0}\033[m \033[1;31mNAO E BISSEXTO!\033[m".format(ano))

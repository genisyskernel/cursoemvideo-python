metros = float(input("\033[1;37mDigite um valor em metros: \033[m"))

c = metros * 100
mm = metros * 1000

print("Metros: \033[0;35m{0}\033[m\nCentimetros: \033[0;33m{1:.0f}\033[m\nMilimetros: \033[0;31m{2:.0f}".format(metros, c, mm))

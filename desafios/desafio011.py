largura = float(input("\033[0;31mInforme a largura da parede em metros: \033[m"))
altura = float(input("\033[0;34mInforme a altura da parede em metros: \033[m"))

area = altura * largura
tinta = area / 2

print("\033[1;30mArea total da parede vale\033[m \033[1;31m{0}\033[m\n\033[1;30mNecessario\033[m \033[1;34m{1}\033[m \033[1;30mlitros de tinta!".format(area, tinta))

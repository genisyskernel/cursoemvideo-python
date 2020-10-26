largura = float(input("Informe a largura da parede em metros: "))
altura = float(input("Informe a altura da parede em metros: "))

area = altura * largura
tinta = area / 2

print("Area total da parede vale {0}\nNecessario {1} litros de tinta!".format(area, tinta))

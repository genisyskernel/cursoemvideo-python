qtd_cedula50 = qtd_cedula20 = qtd_cedula10 = qtd_cedula01 = total = 0

while True:
    print("_="*10)
    print("{0:10}".format("BANCO CURSO EM VIDEO"))
    print("_="*10)

    valor = int(input("Informe o valor para sacar R$? "))

    total = valor

    while total / 50 >= 1:
        qtd_cedula50 += 1
        total -= 50

    while total / 20 >= 1:
        qtd_cedula20 += 1
        total -= 20

    while total / 10 >= 1:
        qtd_cedula10 += 1
        total -= 10

    while total / 1 >= 1:
        qtd_cedula01 += 1
        total -= 1

    print("=-"*20)
    if qtd_cedula50 != 0:
        print(f"Total de {qtd_cedula50} cedulas de R$: 50,00 reais!")
    if qtd_cedula20 != 0:
        print(f"Total de {qtd_cedula20} cedulas de R$: 20,00 reais!")
    if qtd_cedula10 != 0:
        print(f"Total de {qtd_cedula10} cedulas de R$: 10,00 reais!")
    if qtd_cedula01 != 0:
        print(f"Total de {qtd_cedula01} cedulas de R$: 1,00 reais!")
    print("-="*20)
    break
print("Tenha um bom dia!")

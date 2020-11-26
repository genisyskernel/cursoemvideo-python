while True:
    print("_="*10)
    print("{0:10}".format("BANCO CURSO EM VIDEO"))
    print("_="*10)

    valor = int(input("Informe o valor para sacar R$? "))

    qtd_cendula50 = (valor / 50)
    qtd_cendula20 = (qtd_cendula50 / 20)
    qtd_cendula10 = (qtd_cendula20 / 10)
    qtd_cendula01 = (valor / 1)

    print(f"Total de {qtd_cendula50} cedulas de R$: 50,00 reais!")

    print(f"Total de {qtd_cendula20} cedulas de R$: 20,00 reais!")

    print(f"Total de {qtd_cendula10} cedulas de R$: 10,00 reais!")

    print(f"Total de {qtd_cendula01} cedulas de R$: 1,00 reais!")

    break
print("Tenha um bom dia!")


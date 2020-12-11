continuar = nome = produto_mais_barato_nome = ""
preco = total = tot_mais_1000 = produto_mais_barato_preco = cont = 0

while continuar != "N":
    print("<+>" * 8)
    print("LOJA DO CURSO EM VIDEO")
    print("<+>" * 8)

    cont += 1

    nome = str(input("Informe o nome do produto para cadastrar: "))

    while preco <= 0:
        preco = float(input("Informe o preco do produto R$: "))

    while continuar != "S" and continuar != "N":
        continuar = str(input("Deseja continuar [ S/N ]? ")).strip().upper()[0]

    if cont == 1:
        produto_mais_barato_nome = nome
        produto_mais_barato_preco = preco
    else:
        if preco < produto_mais_barato_preco:
            produto_mais_barato_nome = nome

    total += preco

    if preco > 1000:
        tot_mais_1000 += 1

    if continuar == "N":
        break
    else:
        preco = 0
        nome = ""
        continuar = ""

print("=-="*20)
print(f"O total gasto nas compras foi de R$: {total:.2f}!")
print(f"Sao {tot_mais_1000} produtos que custam mais de R$: 1.000,00 reais!")
print(f"O produto {produto_mais_barato_nome} e o mais BARATO que custa R$: {produto_mais_barato_preco}!")

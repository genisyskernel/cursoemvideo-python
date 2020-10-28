preco = float(input("Digite o preco do produto? R$"))

novo_preco = preco - (preco * 0.05)

print("Preco normal R$:{0}\nPreco com 5% de desconto R$: {1:.2f}".format(preco, novo_preco))

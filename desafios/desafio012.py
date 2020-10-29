preco = float(input("Digite o preco do produto? R$"))

novo_preco = preco - (preco * 5 / 100) # 5% de R$ 10 reais : (10*5/100)

print("Preco normal R$: {0:.2f}\nPreco com 5% de desconto R$: {1:.2f}".format(preco, novo_preco))

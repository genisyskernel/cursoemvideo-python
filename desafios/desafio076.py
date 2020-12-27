produtos = ("Notebook", 2500.00, "Microfone", 550.00, "Mouse", 350.00, "Teclado", 400.00, "Mouse Pad", 120.00, "Webcam", 99.90)

print("-"*43)
print(f"{'LISTAGEM DE PREÇOS':^43}")
print("-"*43)

for item in range(0, len(produtos), 2):
    preco = item + 1
    if preco < len(produtos):
        print(f"{produtos[item]:.<30} R$: {produtos[preco]:>7.2f}")
print("-"*43)

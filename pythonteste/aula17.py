"""num = [2, 5, 9, 1]
num[2] = 3
num.append(1)
num.sort(reverse=True)
print(num)
num.pop(2)
num.insert(3, 10)
print(num)
print(f"Essa lista tem {len(num)} itens!")
"""
"""
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for p, v in enumerate(valores):
    print(f"Na posição {p} encontrei o valor {v}...")
print("Cheguei ao final da lista!")
"""
"""
valores = []

for cont in range(1, 6):
    valores.append(int(input("Digite um valor: ")))
print(valores)
"""
"""
# Lista sendo igualadas se tornam uma ligacao entre elas, sendo assim os valores modificados sao em ambas;
a = [2, 4, 5, 8]
b = a
b[1] = 0
print(f"Lista A: {a}")
print(f"Lista B: {b}")
"""
"""
# a[:] Sendo igualada dessa forma o python nao cria uma ligacao com a outra lista apenas copia os valores para a outra;
a = [2, 4, 5, 8]
b = a[:]
b[1] = 0
print(f"Lista A: {a}")
print(f"Lista B: {b}")
"""


"""n = s = 0
while True:
    n = int(input("Digite um numero: "))
    if n == 999:
        break
    s += n
# print("A soma vale {0}!".format(s))
print(f"A soma vale {s}!")

nome = "Jose"
idade = 33
print(f"O {nome} tem {idade} anos!") # PYTHON 3.6 em diante
print("O {} tem {} anos!".format(nome, idade))
print("O %s tem %d anos!" % (nome, idade)) # PYTHON 2
"""
nome = "Jose"
idade = 33
salario = 987.35

print(f"O {nome:20} tem {idade} anos e ganha R$: {salario:.2f}!")

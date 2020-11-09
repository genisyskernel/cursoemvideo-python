peso_maior = 0
peso_menor = 1000

for c in range(0, 5):
    peso = float(input("Informe o seu peso: "))
    if(peso > peso_maior):
        peso_maior = peso
    if(peso < peso_menor):
        peso_menor = peso

print("O peso MAIOR e {0}!".format(peso_maior))
print("O peso MENOR e {0}!".format(peso_menor))

peso_maior = 0
peso_menor = 0

for c in range(1, 6):
    peso = float(input("Informe o peso da {0} pessoa: ".format(c)))
    if(c == 1):
        peso_maior = peso
        peso_menor = peso
    else:
        if(peso > peso_maior):
            peso_maior = peso
        if(peso < peso_menor):
            peso_menor = peso

print("O peso MAIOR e {0}Kg!".format(peso_maior))
print("O peso MENOR e {0}Kg!".format(peso_menor))

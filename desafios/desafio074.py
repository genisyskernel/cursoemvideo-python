from random import randint

maior = menor = 0

num_aleatorio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

for c in range(0, 5):

    if c == 0:
        maior = num_aleatorio[c]
        menor = num_aleatorio[c]
        print(maior)
        print(menor)
    else:
        if num_aleatorio[c] > maior:
            maior = num_aleatorio[c]
        if num_aleatorio[c] < menor:
            menor = num_aleatorio[c]

print(f"Números sorteados foram: {num_aleatorio}")
print(f"O número menor é: {menor}")
print(f"O número maior é: {maior}")

# max e min - Verifica o maior e menor valor dentro da tupla;
#print(f"O número menor é: {min(num_aleatorio)}")
#print(f"O número maior é: {max(num_aleatorio)}")

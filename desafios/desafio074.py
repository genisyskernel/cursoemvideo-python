from random import randint

maior = menor = 0
formatar_numeros = ""

for c in range(0, 5):
    num_aleatorio = randint(1, 10)
    formatar_numeros += f"{num_aleatorio} "

    if c == 0:
        maior = num_aleatorio
        menor = num_aleatorio
    else:
        if num_aleatorio > maior:
            maior = num_aleatorio
        if num_aleatorio < menor:
            menor = num_aleatorio

tupla_numeros = (formatar_numeros)
print(f"Números sorteados foram: {tupla_numeros}")
print(f"O número menor é: {menor}")
print(f"O número maior é: {maior}")

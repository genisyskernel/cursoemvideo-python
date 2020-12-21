formatar_numeros = numeros_pares = ""
numero = cont_9 = cont_3 = cont_pares = 0

for c in range(1, 5):
    numero = int(input(f"Digite o {c} número: "))
    formatar_numeros += f"{numero}"

    if numero == 9:
        cont_9 += 1
    if numero == 3:
        cont_3 += 1
    if numero % 2 == 0:
        numeros_pares += f"{numero} "
        cont_pares += 1

tupla_numeros = tuple(formatar_numeros)

print(f"Você digitou os valores {tupla_numeros}.")
print(f"O número 9 apareceu {cont_9} vezes.")
if cont_3 == 0:
    print("O valor 3 não foi digitado!")
else:
    pos = tupla_numeros.index("3") + 1
    print(f"O primeiro valor 3 foi digitado na {pos}ª posição .")
if cont_pares == 0:
    print("Não teve números pares.")
else:
    print(f"Os números pares são {numeros_pares}.")

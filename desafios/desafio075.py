cont_9 = cont_3 = cont_pares = 0
numeros_pares = ""

tupla_numeros = (int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")),
              int(input("Digite o terceiro número: ")), int(input("Digite o quarto número: ")))

for c in range(0, 4):
    
    if tupla_numeros[c] == 9:
        cont_9 += 1
    if tupla_numeros[c] == 3:
        cont_3 += 1
    if tupla_numeros[c] % 2 == 0:
        numeros_pares += f"{tupla_numeros[c]} "
        cont_pares += 1

print(f"Você digitou os valores {tupla_numeros}.")
print(f"O número 9 apareceu {cont_9} vezes.")
#print(f"O número 9 apareceu {tupla_numeros.count(9)} vezes.")
if cont_3 == 0:
    print("O valor 3 não foi digitado!")
else:
    pos = tupla_numeros.index(3) + 1
    print(f"O primeiro valor 3 foi digitado na {pos}ª posição .")
"""
if 3 in tupla_numeros:
    pos = tupla_numeros.index(3) + 1
    print(f"O primeiro valor 3 foi digitado na {pos}ª posição .")
else:
    print("O valor 3 não foi digitado!")
"""
if cont_pares == 0:
    print("Não teve números pares.")
else:
    print(f"Os números pares são {numeros_pares}.")

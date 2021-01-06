valores = []

menor = maior = c = posicao_maior = posicao_menor = 0

for c in range(0, 5):
    valores.append(int(input(f"Digite o valor da posição {c}: ")))    
    
    if c == 1:
        maior = valores[c]
        menor = valores[c]
    else:

        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print(f"Você digitou os valores: {valores}")
print(f"Maior valor: {maior} | Suas posições: ", end="")
for pos, valor in enumerate(valores):
    if valor == maior:
        print(f"{pos}...", end="")
print()
print(f"Menor valor: {menor} | Suas posições: ", end="")
for pos, valor in enumerate(valores):
    if valor == menor:
        print(f"{pos}...", end="")
print()
            
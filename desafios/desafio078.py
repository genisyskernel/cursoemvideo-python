valores = []

menor = maior = c = posicao_maior = posicao_menor = 0

for c in range(1, 6):
    valores.append(int(input(f"Digite o {c} valor: ")))    
    
    if c == 1:
        maior = valores[0]
        menor = valores[0]
    else:

        for pos, valor in enumerate(valores):
            
            if valor > maior:
                maior = valor
                posicao_maior = pos
            if valor < menor:
                menor = valor
                posicao_menor = pos

# [ 1,  2,  1,  5,  5 ]
#   0 - 1 - 2 - 3 - 4

cont = 0
cont2 = 4
while cont <= 4:
        
    cont += 1
    while cont2 >= 0:
        if valores[cont] == valores[cont2]:
            print(valores[cont])
        cont2 -= 1

print(f"Você digitou os valores: {valores}")
print(f"Maior valor: {maior} | Suas posições: {posicao_maior}.")
print(f"Menor valor: {menor} | Suas posições: {posicao_menor}.")

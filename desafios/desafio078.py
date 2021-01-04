valores = []

menor = maior = 0
posicao_maior = posicao_menor = ""

for c in range(1, 6):
    valores.append(int(input(f"Digite o {c} valor: ")))    
    
    if c == 1:
        maior = valores[0]
        menor = valores[0]
    else:
        for pos, valor in enumerate(valores):
            if valor > maior:
                maior = valor
                posicao_maior = f"{pos}"
            if valor < menor:
                menor = valor
                posicao_menor = f"{pos}"
        
print(f"Maior valor: {maior} | Sua posição: {posicao_maior}.")
print(f"Menor valor: {menor} | Sua posição: {posicao_menor}.")
                

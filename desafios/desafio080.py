valores = []
maior = menor = t = 0

for cont in range(0, 5):
    valor = int(input("Digite um valor: "))
    
    if cont == 0:
        maior = menor = valor
        valores.append(valor)
        print("Valor inserido no final da lista!")
    else:    
        if valor > maior:
            
            maior = valor
            valores.append(valor)
            print("Valor inserido no final da lista!")
            
        if valor < menor:
            
            menor = valor
            valores.insert(0, valor)
            print("Valor inserido na posição 0 da lista!")
            
        if valor > menor and valor < maior:
            
            i = len(valores) - t
            valores.insert(i, valor)
            print(f"Valor inserido na posição {i} da lista!") 
        t += 1

print(f"Os valores digitados em ordem foram: {valores}")
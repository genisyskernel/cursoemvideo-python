valores = valores_em_ordem = []
continuar = ""
cont = 0
duplicado = False

while True:

    if continuar == "N":
        break
    
    valor = int(input("Digite um valor: "))
    
    for c in range(0, len(valores)):
        if valores[c] == valor:
            print("Valor duplicado! Não foi adicionado...")
            duplicado = True
            
    if duplicado == False:
        print("Valor inserido com sucesso!")
        valores.append(valor)
        
    continuar = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    
    duplicado = False
    
    cont += 1
    
print("=-"*30)
valores.sort()
print(f"Você digitou os números: {valores}")
print("FIM DO PROGRAMA")

valores = []
continuar = "S"
cont = 0

while "S" in continuar:
    valor = int(input("Digite um valor: "))

    if cont == 0:
        print(f"Valor adicionado com sucesso!")
        valores.append(valor)
            
    continuar = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
    
    cont += 1

print(f"Você digitou os valores: {valores}")
print("FIM DO PROGRAMA")

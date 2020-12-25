numero_por_extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", 
                      "sete", "oito", "nove", "dez", "onze", "doze", "treze", 
                      "catorze", "quinze", "dezesseis", "dezesete", "dezoito", 
                      "dezenove", "vinte")

sair = "N"

while sair == "N":
    numero = int(input("Digite um número entre 0 e 20: "))
    
    while numero < 0 or numero > 20:
        numero = int(input("Tente novamente. Digite um número entre 0 e 20: "))
    
    print(f"Você digitou o número {numero_por_extenso[numero]}!")

    
    sair = str(input("Deseja sair? [S/N]: ")).strip().upper()[0]
    
    if sair == "S":
        break
print("SAINDO... BYE!")

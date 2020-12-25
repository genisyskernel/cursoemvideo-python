numero_por_extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezesete", "dezoito", "dezenove", "vinte")

numero = int(input("Digite um número entre 0 e 20: "))

while numero < 0 or numero > 20:
    print("Tente novamente. ", end="")
    numero = int(input("Digite um número entre 0 e 20: "))

print(f"Você digitou o número {numero_por_extenso[numero]}!")

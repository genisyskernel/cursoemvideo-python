mais_18 = homens = mulheres_20 = idade = 0
sexo = continuar = ""

while continuar != "N":
    print("*-*"*10)
    print("      CADASTRO DE PESSOA      ")
    print("*-*"*10)

    while idade <= 0 or idade > 120:
        idade = int(input("IDADE: "))

    while sexo != "F" and sexo != "M":
        sexo = str(input("SEXO [ M/F ]: ")).strip().upper()[0]

    print("=-="*10)

    if idade > 18:
        mais_18 += 1

    if sexo == "M":
        homens += 1
    elif idade > 20:
        mulheres_20 += 1

    while continuar != "S" and continuar != "N":
        continuar = str(input("Deseja continuar [ S/N ]? ")).strip().upper()[0]

    if continuar == "N":
        break
    else:
        sexo = ""
        continuar = ""
        idade = 0

print(f"Tem {mais_18} pessoas maiores de 18 anos!")
print(f"E tambem {homens} homens cadastrados.")
print(f"Mulheres maiores de 20 anos tem {mulheres_20}!")

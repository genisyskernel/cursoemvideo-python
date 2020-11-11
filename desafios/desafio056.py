media_idade = 0
soma_idade = 0
maior_idade = 0
nome_maior_idade = ""
cont_menor_idade = 0

for c in range(1, 5):
    print("=-"*5, end="")
    print(" {0}* PESSOA ".format(c), end="")
    print("=-"*5, end="\n")
    nome = str(input("Digite seu nome: ")).strip()
    idade = int(input("Informe sua idade: "))
    sexo = str(input("Informe seu sexo ( M / F ): ")).strip()

    soma_idade += idade
    if(idade > maior_idade and sexo in "Mm"):
        maior_idade = idade
        nome_maior_idade = nome
    if(idade < 20 and sexo in "Ff"):
        cont_menor_idade += 1

media_idade = soma_idade / 4
print("A media de idade do grupo e {0:.2f} anos.".format(media_idade))
print("O nome do homem mais velho e {0} e tem {1} anos.".format(nome_maior_idade, maior_idade))
print("Ao todo sao {0} mulheres com menos de 20 anos.".format(cont_menor_idade))

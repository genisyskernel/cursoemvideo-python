media_idade = 0
soma_idade = 0
maior_idade = 0
nome_maior_idade = ""
cont_menor_idade = 0

for c in range(0, 4):
    nome = str(input("Digite seu nome: "))
    idade = int(input("Informe sua idade: "))
    sexo = str(input("Informe seu sexo ( M / F ): "))

    soma_idade += idade
    if(idade > maior_idade and sexo == "M"):
        maior_idade = idade
        nome_maior_idade = nome
    if(idade < 20 and sexo == "F"):
        cont_menor_idade += 1

media_idade = soma_idade / 4
print("A media de idade do grupo: {0:.2f}.".format(media_idade))
print("O nome do homem mais velho: {0}.".format(nome_maior_idade))
print("Quantidade de mulheres que tem menos de 20 anos: {0}.".format(cont_menor_idade))

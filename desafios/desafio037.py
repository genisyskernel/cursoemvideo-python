num = int(input("Digite um numero inteiro: "))

base_conversao = int(input("Digite o numero para conversao ( 1 = BINARIO | 2 = OCTAL | 3 = HEXADECIMAL ): "))

divisao_inteira = num
resto_divisao = num
binario = ""
octal = ""

if base_conversao == 1:
    while divisao_inteira != 0:

        resto_divisao = divisao_inteira

        divisao_inteira = (divisao_inteira // 2)

        resto_divisao = (resto_divisao % 2)

        binario = str(resto_divisao) + binario

    print("O numero {0} em binario e {1}.".format(num, binario))

elif base_conversao == 2:
    print("OCTAL")

elif base_conversao == 3:
    print("HEXADECIMAL")

else:
    print("Base invalida!")

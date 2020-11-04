num = int(input("Digite um numero inteiro: "))

base_conversao = int(input("Digite o numero para conversao ( 1 = BINARIO | 2 = OCTAL | 3 = HEXADECIMAL ): "))

if base_conversao == 1:
    divisao_inteira = num
    resto_divisao = num
    binario = ""
    while divisao_inteira != 0:

        resto_divisao = divisao_inteira

        divisao_inteira = (divisao_inteira // 2)

        resto_divisao = (resto_divisao % 2)

        binario = str(resto_divisao) + binario

    print("O numero {0} em BINARIO e {1}.".format(num, binario))

elif base_conversao == 2:
    divisao_inteira = num
    resto_divisao = num
    octal = ""
    while divisao_inteira != 0:

        resto_divisao = divisao_inteira

        divisao_inteira = (divisao_inteira // 8)

        resto_divisao = (resto_divisao % 8)

        octal = str(resto_divisao) + octal

    print("O numero {0} em OCTAL e {1}.".format(num, octal))

elif base_conversao == 3:
    divisao_inteira = num
    resto_divisao = num
    hexadecimal = ""
    while divisao_inteira != 0:

        resto_divisao = divisao_inteira

        divisao_inteira = (divisao_inteira // 16)

        resto_divisao = (resto_divisao % 16)

        if(resto_divisao > 9):
            if(resto_divisao == 10):
                resto_divisao = "A"
            elif(resto_divisao == 11):
                resto_divisao = "B"
            elif(resto_divisao == 12):
                resto_divisao = "C"
            elif(resto_divisao == 13):
                resto_divisao = "D"
            elif(resto_divisao == 14):
                resto_divisao = "E"
            else:
                resto_divisao = "F"

        hexadecimal = str(resto_divisao) + hexadecimal

    print("O numero {0} em HEXADECIMAL e {1}.".format(num, hexadecimal))

else:
    print("Base invalida!")

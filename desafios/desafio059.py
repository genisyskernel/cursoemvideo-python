sair = False
resultado = 0

while sair == False:

    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))

    print("[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NUMEROS\n[ 5 ] SAIR\n", end="")
    opcao = int(input("Qual operacao realizar? "))

    if(opcao == 1):
        resultado = num1 + num2
    elif(opcao == 2):
        resultado = num1 * num2
    elif(opcao == 3):
        if(num1 > num2):
            resultado = num1
        else:
            resultado = num2
    elif(opcao == 4):
        print("ESCOLHENDO NOVOS NUMEROS...")
    elif(opcao == 5):
        print("SAINDO...")
        sair = True
    else:
        print("Opcao invalida! Tente novamente!")

    if(opcao != 4 and opcao != 5 and opcao >= 1 and opcao <= 3):
        print("Opcao escolhida: [ {0} ]".format(opcao))
        print("Resultado: {0}!".format(resultado))

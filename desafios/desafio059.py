from time import sleep
opcao = 0
resultado = 0

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
while opcao != 5:

    print("[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NUMEROS\n[ 5 ] SAIR\n", end="")
    opcao = int(input("Qual operacao realizar? "))

    if(opcao == 1):
        resultado = num1 + num2
        print("Resultado entre {0} + {1} = {2}!".format(num1, num2, resultado))
    elif(opcao == 2):
        resultado = num1 * num2
        print("Resultado entre {0} x {1} = {2}!".format(num1, num2, resultado))
    elif(opcao == 3):
        if(num1 > num2):
            resultado = num1
        else:
            resultado = num2

        print("O maior entre {0} e {1} = {2}!".format(num1, num2, resultado))
    elif(opcao == 4):
        print("ESCOLHENDO NOVOS NUMEROS...")
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
    elif(opcao == 5):
        print("SAINDO...")
    else:
        print("Opcao invalida! Tente novamente!")
    print("=-=" * 10)
    sleep(2)

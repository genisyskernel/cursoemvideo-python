altura = float(input("Informe sua altura: "))

peso = float(input("Informe seu peso: "))

imc = peso / (altura * 2)

if(imc <= 18.5):
    situacao = "ABAIXO DO PESO"
elif(18.5 >= imc <= 25):
    situacao = "PESO IDEAL"
elif(25 >= imc <= 30):
    situacao = "SOBREPESO"
elif(30 >= imc <= 40):
    situacao = "OBESIDADE"
else:
    situacao = "OBESIDADE MORBIDA"

print("Sua altura: {0:.2f} metros.\nSeu peso: {1:.2f} kilos.\nIMC: {2}!".format(altura, peso, situacao))

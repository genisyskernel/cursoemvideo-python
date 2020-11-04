nota01 = float(input("Digite a primeira nota: "))
nota02 = float(input("Digite a segunda nota: "))

media = (nota01 + nota02) / 2

if(media >= 7.0):
    situacao = "Voce foi \033[1;32mAPROVADO\033[m!"
elif(6.9 >= media >= 5.0):
    situacao = "Voce esta em \033[1;31mRECUPERACAO\033[m!"
else:
    situacao = "Voce esta \033[1;31mREPROVADO\033[m!"

print(situacao)
print("Media de {0:.2f} das notas {1:.2f} e {2:.2f}.".format(media, nota01, nota02))

frase = str(input("Digite uma frase qualquer: "))

frase_original = frase.strip().replace(" ", "").upper()
frase_nova = ""

frase_nova = frase_original[::-1]
'''for c in range(len(frase_original), 0, -1):
    frase_nova += frase_original[c - 1]'''

print("O inverso de {0} e {1}.".format(frase_original, frase_nova))
if(frase_nova == frase_original):
    print("A frase E PALINDROMO!")
else:
    print("A frase NAO E PALINDROMO!")

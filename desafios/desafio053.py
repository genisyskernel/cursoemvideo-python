frase = str(input("Digite uma frase qualquer: "))

frase_original = frase.strip().replace(" ", "")
frase_nova = ""

# APOSASOPA
# TESTETESTE

for c in range(len(frase_original), 0, -1):
    frase_nova = frase_nova + frase_original[c - 1]

if(frase_nova == frase_original):
    print("A frase E PALINDROMO!")
else:
    print("A frase NAO E PALINDROMO!")

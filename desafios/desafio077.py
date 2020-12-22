palavras = ("Arroz", "Feijao", "Computador", "Moto", "Mouse", "Video", "Mesa", "Aprender")

for palavra in palavras:
    print(f"A palavra {palavra.upper()} tem as vogais: ", end="")
    for letra in range(0, len(palavra)):
        if palavra[letra].upper() in "AEIOU":
            print(f"{palavra[letra].lower()}", end=" ")
    print()

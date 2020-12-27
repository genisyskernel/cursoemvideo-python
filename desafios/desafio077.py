palavras = ("Arroz", "Feijao", "Computador", "Moto", "Mouse", "Video", "Mesa", "Aprender")

for palavra in palavras:
    print(f"A palavra {palavra.upper()} tem as vogais: ", end="")
    for letra in palavra:
        if letra.upper() in "AEIOU":
            print(f"{letra.lower()}", end=" ")
    print()

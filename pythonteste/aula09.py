frase = "Curso em Video Python"

print("""   Texto
Grande 
    Em 
        Varias
Linhas!""")

# Fatiamento
print(frase[9])
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

# Analise
print(len(frase)) # Mostra o tamanho da String
print(frase.count("o")) # Conta quantos "o" tem na String
print(frase.count("o", 0, 13)) # Conta quantos "o" tem na String com fatiamento
print(frase.find("deo")) # Mostraem que posicao a sequencia "deo" comeca na String
print(frase.find("Android")) # Retorna a posicao -1 que nao existe na String
print("Curso" in frase) # Retorna True que existe a sequencia na String

# Transformacao
print(frase.replace("Python", "Android"))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase = "   Aprenda Python  "
print(frase.strip()) # Remove os espacos do comeco e final da String
print(frase.rstrip()) # (r = right) Mantem os espacos no comeco e so remove os do final da String
print(frase.lstrip()) # (l = left ) Mantem os espacos do final e remove os do comeco da String

# Divisao
frase = "Curso em Video Python"
print(frase.split()) # Divide a String considerando os espacos para dividir por palavras e coloca em uma lista
dividido = frase.split()
print(dividido[0])
print(dividido[0][3])

# Juncao
print("-".join(frase))

# Juntando metodos
print(frase.upper().count("O"))
print(frase.lower().find("video"))


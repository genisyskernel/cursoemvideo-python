"""
nome = str(input("Digite seu nome: "))

if( nome == "Eduardo"):
    print("Que nome bonito voce tem! Bom dia {0}!".format(nome))
else:
    print("Bom dia, {0}!".format(nome))

print("===FIM===")
"""

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

m = (n1 + n2) / 2

if m < 6.0:
    aviso = "muito ruim"
elif 6.0 <= m <= 7.0:
    aviso = "boa"
else:
    aviso = "excelente"

print("A sua media foi {:.1f}".format(m))
print("Sua media foi {0}!".format(aviso))

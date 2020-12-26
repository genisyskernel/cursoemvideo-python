tabela_brasileirao = ("Corinthians", "Palmeiras", "Santos", "Grêmio", "Cruzeiro", "Flamengo", "Vasco da Gama", "Chapecoense", "Atlêtico Mineiro", "Botafogo", "Athletico-PR", "Bahia", "São Paulo", "Fluminense", "Sport Recife", "Vitória", "Coritiba", "Avaí", "Ponte Preta", "Atlético Goianiense")

# A
print("*="*50)
print(f"Lista dos 5 primeiros times: {tabela_brasileirao[0:5]}")
print("*="*50)
# B
print(f"Últimos 4 times colocados: {tabela_brasileirao[-4:]}")
print("*="*50)
# C
print(f"Times em ordem alfabética: {sorted(tabela_brasileirao)}")
print("*="*50)
# D
print(f"O time da Chapecoense está na {tabela_brasileirao.index('Chapecoense') + 1}º posição!")
print("*="*50)

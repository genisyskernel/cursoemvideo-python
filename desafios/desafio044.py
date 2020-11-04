valor_produto = float(input("Informe o valor do produto R$ "))
condicao_pagamento = int(input("1 = A VISTA 10% DE DESCONTO NO DINHEIRO/CHEQUE"
                               "\n2 = A VISTA 5% DE DESCONTO NO CARTAO"
                               "\n3 = 2x SEM JUROS NO CARTAO"
                               "\n4 = 3x COM JUROS DE 20% NO CARTAO"
                               "\nQual vai ser a condicao do pagamento? "))

valor_produto_novo = valor_produto

if(condicao_pagamento == 1):
    valor_produto_novo = valor_produto - valor_produto*10/100
elif(condicao_pagamento == 2):
    valor_produto_novo = valor_produto - valor_produto*5/100
elif(condicao_pagamento == 4):
    valor_produto_novo = valor_produto + valor_produto*20/100

print("O produto no valor de R$ {0:.2f} vai ficar por R$ {1:.2f}!".format(valor_produto, valor_produto_novo))

print("{0:=^40}".format(" LOJA DO GAFANHOTO "))
valor_produto = float(input("Informe o valor das compras R$ "))
condicao_pagamento = int(input("1 = A VISTA 10% DE DESCONTO NO DINHEIRO/CHEQUE"
                               "\n2 = A VISTA 5% DE DESCONTO NO CARTAO"
                               "\n3 = 2x SEM JUROS NO CARTAO"
                               "\n4 = 3x OU MAIS COM JUROS DE 20% NO CARTAO"
                               "\nQual vai ser a condicao do pagamento? "))

valor_produto_novo = valor_produto

if(condicao_pagamento == 1):
    valor_produto_novo = valor_produto - valor_produto*10/100
elif(condicao_pagamento == 2):
    valor_produto_novo = valor_produto - valor_produto*5/100
elif(condicao_pagamento == 3):
    valor_produto_novo = valor_produto
    valor_parcela = valor_produto_novo / 2
    print("Sua compra esta parcelada em 2x de R$ {0:.2f} reais SEM JUROS!".format(valor_parcela))
elif(condicao_pagamento == 4):
    qtd_parcelas = int(input("Quantas parcelas? "))
    valor_produto_novo = valor_produto + valor_produto * 20 / 100
    valor_parcela = valor_produto_novo / qtd_parcelas
    print("Sua compra esta parcelada em {0}x de R$ {1:.2f} reais COM JUROS!".format(qtd_parcelas, valor_parcela))
else:
    valor_produto_novo = valor_produto
    print("OPCAO INVALIDA de pagamento! Tente novamente!")

print("O produto no valor de R$ {0:.2f} vai ficar por R$ {1:.2f}!".format(valor_produto, valor_produto_novo))

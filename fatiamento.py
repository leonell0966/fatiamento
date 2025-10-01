dados_pedido = "COD:01234|PRODUTO:Coleira Personalizada|QUANTIDADE:2|PRECO_UNITARIO:25.50|STATUS:EM PROCESSAMENTO"
url_dados=dados_pedido[0:9]
print(url_dados)
coleira=dados_pedido[18:39]
print(f"produto :{coleira}")
#etapa 2: manipulando e formatando Dados
qtd=dados_pedido[19:50]
#calcule o preco total
url_qtde=dados_pedido[51]
#print(url_qtde)
url_uni=dados_pedido[68:73]
#print(url_uni)
#quantidades_str=dados_pedido[url_qtde:url_uni]
#quantidade=int(quantidades_str)
quantidade1=int(url_qtde)
#print(quantidade1)
#qtde_total=url_qtde*url_uni
#print(qtde_total)
quantidade2=float(url_uni)
#print(quantidade2)
preco_total=quantidade1*quantidade2
print(f"valor total :{preco_total}")
#exibir meu processamento
url_proc=dados_pedido[74:97]
url_padronizados=url_proc.lower()
print(url_padronizados)
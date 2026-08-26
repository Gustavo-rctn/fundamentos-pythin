def encontrar_produto(produtos, produto):
    return produtos.index(produto)

lista_produtos = ['Arroz', 'Feijão', 'Macarrão', 'Café']
posicao = encontrar_produto(lista_produtos, 'Macarrão')
print(f"Ex 6 - 'Macarrão' está no índice: {posicao}")
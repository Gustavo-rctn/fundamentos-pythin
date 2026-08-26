def remover_produtos(produto, produtos):
    produtos.remove(produto)
    print(f'O produto {produto} foi removido')

lista_produtos = ['Arroz', 'Feijão', 'Refrigerante', 'Chocolate']
remover_produtos('Arroz', lista_produtos)
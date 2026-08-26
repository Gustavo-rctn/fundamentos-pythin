def remover_item(item, posicao):
    if item == posicao:
        remover_item(item, posicao)
        print(f'{item} não foi removido')
    else:
        print(f'{item} foi removido')


lista_item = ['Arroz', 'Feijão', 'Agua', 'Guilherme']
remover_item(lista_item[1], [1])
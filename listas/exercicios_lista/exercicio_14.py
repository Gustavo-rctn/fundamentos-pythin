def adicionar_produtos(compras, novos_produtos):
    compras.extend(novos_produtos)

def cancelar_compra(compras, produto):
    compras.remove(produto)

minhas_compras = ['Leite', 'Pão']
adicionar_produtos(minhas_compras, ['Manteiga', 'Queijo'])
print(f"\nEx 14 - Compras atualizadas: {minhas_compras}")

cancelar_compra(minhas_compras, 'Pão')
print(f"Ex 14 - Após cancelar 'Pão': {minhas_compras}")
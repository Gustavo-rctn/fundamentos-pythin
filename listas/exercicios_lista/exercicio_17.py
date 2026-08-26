estoque = ["Mouse", "Teclado", "Monitor", "Webcam"]

def vender_produto(estoque, produto):
    if produto in estoque:
        estoque.remove(produto)
        print(f"Venda realizada: {produto}")
    else:
        print(f"O produto '{produto}' não está disponível.")
    return estoque

print("\nEx 17 - Teste de Estoque:")
vender_produto(estoque, "Teclado")
vender_produto(estoque, "Impressora")
print(f"Estoque final: {estoque}")
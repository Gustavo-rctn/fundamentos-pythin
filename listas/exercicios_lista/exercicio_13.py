def adicionar_cliente(fila, cliente):
    fila.append(cliente)

def atender_cliente(fila):
    return fila.pop(0)

# Demonstração da Fila:
fila_banco = []
adicionar_cliente(fila_banco, "Cliente 1 - Marcos")
adicionar_cliente(fila_banco, "Cliente 2 - Julia")
print(f"\nEx 13 - Fila criada: {fila_banco}")

atendido = atender_cliente(fila_banco)
print(f"Ex 13 - Cliente atendido: {atendido}")
print(f"Ex 13 - Fila restante: {fila_banco}")
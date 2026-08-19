def contar_pares(inicio, fim):
    qtd = 0
    for i in range(inicio, fim + 1):
        if i % 2 == 0:
            qtd += 1
    return qtd

i = int(input("Digite o valor inicial: "))
f = int(input("Digite o valor final: "))
print(f"Quantidade de pares: {contar_pares(i, f)}")
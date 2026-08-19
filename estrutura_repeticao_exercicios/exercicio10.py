def somar_pares(inicio, fim):
    soma = 0
    for i in range(inicio, fim + 1):
        if i % 2 == 0:
            soma += i
    return soma

i = int(input("Digite o valor inicial: "))
f = int(input("Digite o valor final: "))
print(f"Soma dos pares: {somar_pares(i, f)}")
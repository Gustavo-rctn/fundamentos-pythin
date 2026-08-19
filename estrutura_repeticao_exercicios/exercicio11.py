def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

num = int(input("Digite um número para calcular o fatorial: "))
print(f"Fatorial de {num}: {fatorial(num)}")
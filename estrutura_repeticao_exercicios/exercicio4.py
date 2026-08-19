def mostrar_impares(numero):
    for i in range(1, numero + 1):
        if i % 2 != 0:
            print(i)

num = int(input("Digite um número: "))
mostrar_impares(num)
def caixa_eletronico(valor):
    notas = [100, 50, 20, 10, 5, 2]
    print(f"Notas para o valor de R${valor}:")

    for nota in notas:
        quantidade = valor // nota
        if quantidade > 0:
            print(f"{quantidade} nota(s) de R${nota}")
            valor %= nota


v = int(input("Digite o valor para saque: "))
caixa_eletronico(v)

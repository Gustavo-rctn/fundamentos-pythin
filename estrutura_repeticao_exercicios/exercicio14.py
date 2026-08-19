def calcular_media():
    soma = 0
    quantidade = 0
    while True:
        num = float(input("Digite um número (0 para sair): "))
        if num == 0:
            break
        soma += num
        quantidade += 1

    if quantidade > 0:
        media = soma / quantidade
        print(f"A média dos números digitados é: {media}")
    else:
        print("Nenhum número foi digitado.")


calcular_media()
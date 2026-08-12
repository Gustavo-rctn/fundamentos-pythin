def calcular_desconto():
    valor = float(input("Digite o valor da compra (R$): "))
    if valor <= 100:
        desconto = 0
    elif valor <= 500:
        desconto = 0.10
    else:
        desconto = 0.15

    valor_final = valor * (1 - desconto)
    print(f"Valor final com desconto: R$ {valor_final:.2f}")

calcular_desconto()
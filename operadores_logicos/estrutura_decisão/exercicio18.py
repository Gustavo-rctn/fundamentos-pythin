def calcular_frete():
    valor_compra = float(input("Digite o valor da compra (R$): "))
    if valor_compra <= 100:
        frete = 20.0
    elif valor_compra <= 300:
        frete = 10.0
    else:
        frete = 0.0

    total = valor_compra + frete
    print(f"Frete: R$ {frete:.2f}")
    print(f"Valor total (Compra + Frete): R$ {total:.2f}")

calcular_frete()
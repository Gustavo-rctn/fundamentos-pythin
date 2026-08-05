def calcular_desconto():
    preco = float(input("Digite o preço do produto: "))
    percentual_desconto = float(input("Digite o percentual de desconto (%): "))
    valor_final = preco - (preco * (percentual_desconto / 100))
    print(f"O valor final com desconto é: R$ {valor_final:.2f}")

calcular_desconto()
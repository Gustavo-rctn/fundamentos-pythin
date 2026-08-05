def valor_prestacao():
    preco_produto = float(input("Digite o valor do produto: "))
    parcelas = int(input("Digite a quantidade de parcelas: "))
    valor_parcela = preco_produto / parcelas
    print(f"O valor de cada parcela é: R$ {valor_parcela:.2f}")

valor_prestacao()
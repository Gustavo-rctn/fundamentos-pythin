def consumo_energia():
    consumo_kwh = float(input("Digite o consumo em kWh: "))
    preco_kwh = float(input("Digite o preço do kWh: "))
    valor_conta = consumo_kwh * preco_kwh
    print(f"O valor da conta de energia é: R$ {valor_conta:.2f}")

consumo_energia()
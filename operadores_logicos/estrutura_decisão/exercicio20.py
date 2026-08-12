def caixa_eletronico():
    saldo = float(input("Digite o saldo disponível (R$): "))
    saque = float(input("Digite o valor do saque (R$): "))

    if saque <= 0:
        print("Valor de saque inválido")
    elif saque > saldo:
        print("Saldo insuficiente")
    else:
        novo_saldo = saldo - saque
        print(f"Saque realizado com sucesso! Novo saldo: R$ {novo_saldo:.2f}")

caixa_eletronico()
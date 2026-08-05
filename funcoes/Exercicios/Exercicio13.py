def calcular_comissao():
    salario_fixo = float(input("Digite o salário fixo: "))
    valor_vendas = float(input("Digite o valor das vendas: "))
    percentual_comissao = float(input("Digite o percentual de comissão (%): "))

    comissao = valor_vendas * (percentual_comissao / 100)
    salario_final = salario_fixo + comissao
    print(f"O salário final é: R$ {salario_final:.2f}")


calcular_comissao()
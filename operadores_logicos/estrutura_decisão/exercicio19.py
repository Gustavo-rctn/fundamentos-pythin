def classificar_numero():
    numero = int(input("Digite um número inteiro: "))

    # Sinal
    if numero > 0:
        sinal = "positivo"
    elif numero < 0:
        sinal = "negativo"
    else:
        sinal = "zero"

    # Paridade
    if numero % 2 == 0:
        paridade = "par"
    else:
        paridade = "ímpar"

    if sinal == "zero":
        print("Classificação: zero e par")
    else:
        print(f"Classificação: {sinal} e {paridade}")

classificar_numero()
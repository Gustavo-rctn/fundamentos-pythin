def trocar_valores():
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))

    print(f"\nAntes:\nA = {a}\nB = {b}")

    # Troca de valores
    a, b = b, a

    print(f"\nDepois:\nA = {a}\nB = {b}")


trocar_valores()
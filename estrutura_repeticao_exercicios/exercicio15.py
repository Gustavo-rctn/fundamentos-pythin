def maior_numero():
    maior = None
    continuar = 's'

    while continuar.lower() == 's':
        num = float(input("Digite um número: "))
        if maior is None or num > maior:
            maior = num
        continuar = input("Deseja continuar? (s/n): ")

    return maior


resultado = maior_numero()
if resultado is not None:
    print(f"O maior número digitado foi: {resultado}")
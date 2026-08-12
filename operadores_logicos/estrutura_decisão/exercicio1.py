def verificar_numero():
    numero = int(input("Digite um número inteiro: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Igual a zero")

verificar_numero()
def preco_ingresso():
    idade = int(input("Digite a idade do cliente: "))
    if idade <= 5:
        print("Ingresso Gratuito")
    elif idade <= 12 or idade >= 60:
        print("Preço do ingresso: R$ 10,00")
    else:
        print("Preço do ingresso: R$ 20,00")

preco_ingresso()